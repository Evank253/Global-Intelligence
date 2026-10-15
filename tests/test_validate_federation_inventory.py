import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path

VALIDATOR_PATH = Path(__file__).resolve().parents[1] / "tools" / "validate_federation_evidence.py"
SPEC = importlib.util.spec_from_file_location("validator", VALIDATOR_PATH)
VALIDATOR = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VALIDATOR)

class InventoryDigestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "report.json").write_bytes(b'{"ok":true}')

    def tearDown(self):
        self.tmp.cleanup()

    def entry(self):
        digest = hashlib.sha256((self.root / "report.json").read_bytes()).hexdigest()
        return f"{digest}  report.json"

    def test_matching_digest_passes(self):
        (self.root / "inventory.sha256").write_text(self.entry() + "\n", encoding="utf-8")
        self.assertEqual(VALIDATOR.validate_inventory(self.root, ["report.json"]), 1)

    def test_modified_file_with_stale_digest_fails(self):
        entry = self.entry()
        (self.root / "report.json").write_bytes(b'{"ok":false}')
        (self.root / "inventory.sha256").write_text(entry + "\n", encoding="utf-8")
        with self.assertRaisesRegex(VALIDATOR.ValidationError, "SHA-256 mismatch"):
            VALIDATOR.validate_inventory(self.root, ["report.json"])

    def test_duplicate_path_fails(self):
        entry = self.entry()
        (self.root / "inventory.sha256").write_text(entry + "\n" + entry + "\n", encoding="utf-8")
        with self.assertRaisesRegex(VALIDATOR.ValidationError, "duplicate inventory path"):
            VALIDATOR.validate_inventory(self.root, ["report.json"])

    def test_missing_listed_file_fails(self):
        (self.root / "inventory.sha256").write_text("0" * 64 + "  missing.bin\n", encoding="utf-8")
        with self.assertRaisesRegex(VALIDATOR.ValidationError, "missing or unresolvable"):
            VALIDATOR.validate_inventory(self.root, ["missing.bin"])

if __name__ == "__main__":
    unittest.main()
