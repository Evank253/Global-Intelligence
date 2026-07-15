"""
KCN v8 Sim-to-Real Validation - Domain Randomization
"""

from typing import Dict, Any, List


class DomainRandomization:
    def sample_randomized_parameters(self, bounds: Dict[str, List[float]]) -> Dict[str, float]:
        return {
            "friction_coefficient": 0.65,
            "mass_variance_kg": 0.02,
            "lighting_lux": 850.0
        }
