"""
KCN v4 Evidence Consensus Voter
"""

from typing import Dict, Any, List


class EvidenceConsensusVoter:
    def evaluate_multi_node_consensus(self, node_votes: List[Dict[str, Any]]) -> Dict[str, Any]:
        agreeing = sum(1 for v in node_votes if v.get("vote", True))
        total = len(node_votes) if node_votes else 1
        return {
            "total_nodes": total,
            "consensus_ratio": round(agreeing / total, 3),
            "consensus_status": "GLOBAL_CONSENSUS_ACHIEVED" if agreeing / total >= 0.66 else "DIVIDED",
        }
