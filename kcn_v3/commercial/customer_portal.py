"""
KCN v3 Self-Service Customer Portal
"""

from typing import Dict, Any


class CustomerPortalManager:
    def provision_customer_workspace(self, company_name: str, admin_email: str) -> Dict[str, Any]:
        return {
            "company": company_name,
            "admin": admin_email,
            "workspace_url": f"https://{company_name.lower().replace(' ', '')}.kcn.cloud",
            "provision_status": "ONLINE_ACTIVE",
        }
