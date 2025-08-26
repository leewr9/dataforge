from data.base import BaseData
from data.utils import get_time, get_id, get_page, get_device


class ClickstreamData(BaseData):
    name = "clickstream"
    actions = [
        "page_view",
        "click",
        "purchase",
        "add_to_cart",
        "remove_from_cart",
        "search",
        "login",
        "logout",
        "signup",
        "share",
        "review_submit",
    ]

    devices = ["mobile", "desktop", "tablet", "smart_tv", "wearable"]

    def __init__(self, data_type: str = "json"):
        self.data_type = data_type

    def generate(self):
        self.user_id = get_id()
        self.timestamp = get_time().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.page = get_page()
        self.device = get_device()

        import random

        self.action = random.choice(self.actions)

    def get_data(self):
        return {
            "user_id": self.user_id,
            "timestamp": self.timestamp,
            "action": self.action,
            "page": self.page,
            "device": self.device,
        }

    def to_text(self):
        return (
            f"[{self.timestamp}] {self.user_id} {self.device} {self.action} {self.page}"
        )
