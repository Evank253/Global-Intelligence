#!/usr/bin/env python3
"""
KCN Intelligence OS v4 - Federated Network Node Registration & Provenance Sync
Demonstrates initializing a local KCN node, establishing cryptographic trust handshakes,
and syncing provenance chains across global network peers.
"""

from kcn_v4.federated_intelligence.node_registry import NodeRegistry
from kcn_v4.federated_intelligence.trust_handshake import TrustHandshakeEngine
from kcn_v4.knowledge_network.provenance_chain import GlobalProvenanceChain


def main():
    print("================================================================================")
    print("      KCN v4 GLOBAL INTELLIGENCE NETWORK - NODE FEDERATION DEMO")
    print("================================================================================")

    # 1. Register Node
    node_reg = NodeRegistry()
    node_id = node_reg.register_node("Research_Institute_Alpha", capabilities=["quantum_sim", "bio_swarm"])
    print(f"[Node Registration] Created Node ID: {node_id}")

    # 2. Perform Mutual Trust Handshake
    handshake = TrustHandshakeEngine()
    auth_result = handshake.authenticate_node(node_id, cryptographic_proof="sig_rsa_4096_verified")
    print(f"[Trust Handshake] Authentication Status: {auth_result['status']} | Trust Level: {auth_result['trust_level']}")

    # 3. Log Provenance Block
    prov_chain = GlobalProvenanceChain()
    block = prov_chain.append_block(
        data_payload={"action": "SYNTHESIZE_EPIDEMIC_SURVEILLANCE_MODEL", "node_id": node_id},
        previous_hash="0000000000000000000000000000000000000000000000000000000000000000"
    )
    print(f"[Provenance Chain] New Cryptographic Hash: {block['hash']}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
