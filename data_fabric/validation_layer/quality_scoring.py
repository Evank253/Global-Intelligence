"""
Data Fabric - Data Quality Scorer
Scores incoming data feeds on completeness, source authority, freshness, and signal-to-noise ratios.
"""

from typing import Dict, Any


class DataQualityScorer:
    def compute_quality_score(self, source_authority: float, completeness: float, freshness_age_sec: float) -> Dict[str, Any]:
        freshness_decay = max(0.0, 1.0 - (freshness_age_sec / (86400 * 30)))
        composite_quality = (source_authority * 0.4) + (completeness * 0.4) + (freshness_decay * 0.2)

        return {
            "source_authority": source_authority,
            "completeness": completeness,
            "freshness_decay_factor": round(freshness_decay, 3),
            "quality_score": round(composite_quality, 3),
            "acceptable_for_production": composite_quality >= 0.80,
        }
