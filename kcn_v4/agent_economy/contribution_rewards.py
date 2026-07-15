"""
KCN v4 Contribution Reward Allocator
"""

from typing import Dict, Any


class ContributionRewardAllocator:
    def allocate_token_reward(self, contributor_node: str, impact_score: float) -> Dict[str, Any]:
        reward_units = round(impact_score * 100, 2)
        return {
            "node": contributor_node,
            "tokens_rewarded": reward_units,
            "settlement_status": "ALLOCATED_TO_LEDGER",
        }
