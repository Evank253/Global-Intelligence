"""
Enterprise Billing - Plans Specification
"""

PLANS = {
    "starter": {
        "agents": 5,
        "requests": 10000,
        "storage": "10GB",
    },
    "professional": {
        "agents": 50,
        "requests": 100000,
        "storage": "250GB",
    },
    "enterprise": {
        "agents": "unlimited",
        "requests": "unlimited",
        "storage": "custom",
    },
}


def get_plan(name: str):
    return PLANS.get(name)
