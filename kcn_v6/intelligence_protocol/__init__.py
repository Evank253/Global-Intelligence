"""
KCN v6 - Intelligence Protocol Subpackage
"""

from kcn_v6.intelligence_protocol.message_schema import IntelligenceMessage
from kcn_v6.intelligence_protocol.agent_communication import AgentCommunication
from kcn_v6.intelligence_protocol.capability_protocol import CapabilityProtocol
from kcn_v6.intelligence_protocol.context_exchange import ContextExchange

__all__ = ["IntelligenceMessage", "AgentCommunication", "CapabilityProtocol", "ContextExchange"]
