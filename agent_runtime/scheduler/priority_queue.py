"""
Agent Runtime - Priority Queue Engine
"""

from typing import Dict, Any, List


class PriorityQueueEngine:
    def rank_task_queue(self, tasks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(tasks, key=lambda x: x.get("priority", 1), reverse=True)
