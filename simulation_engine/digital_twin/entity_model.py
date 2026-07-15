"""
Digital Twin System - Entity Model
"""

from typing import Dict, Any


class EntityModel:
    def create_entity(self, entity_id: str, attributes: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "entity_id": entity_id,
            "attributes": attributes,
            "operational": True,
        }
