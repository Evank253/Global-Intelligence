"""
Measurement Engine - Accuracy Metrics
"""

from typing import Dict, Any, List


class AccuracyEvaluator:
    def compute_confusion_matrix(self, predictions: List[bool], ground_truths: List[bool]) -> Dict[str, Any]:
        tp = sum(1 for p, g in zip(predictions, ground_truths) if p and g)
        fp = sum(1 for p, g in zip(predictions, ground_truths) if p and not g)
        fn = sum(1 for p, g in zip(predictions, ground_truths) if not p and g)
        tn = sum(1 for p, g in zip(predictions, ground_truths) if not p and not g)

        total = len(predictions)
        accuracy = (tp + tn) / total if total > 0 else 0.0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0

        return {
            "accuracy": round(accuracy, 4),
            "precision": round(precision, 4),
            "recall": round(recall, 4),
            "false_positive_rate": round(fp / total, 4) if total > 0 else 0.0,
            "false_negative_rate": round(fn / total, 4) if total > 0 else 0.0,
        }
