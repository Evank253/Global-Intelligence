"""
KCN v3 Auditor Report Exporter
"""

from typing import Dict, Any


class AuditorReportExporter:
    def export_pdf_report(self, audit_id: str) -> Dict[str, Any]:
        return {
            "audit_id": audit_id,
            "export_format": "PDF_SOC2_EVIDENCE_PACKAGE",
            "download_url": f"/v1/exports/{audit_id}.pdf",
        }
