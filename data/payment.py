from data.base import BaseData
from data.utils import get_time, get_id


class PaymentsData(BaseData):
    name = "payments"
    methods = [
        "credit_card",
        "paypal",
        "bank_transfer",
        "kakao_pay",
        "naver_pay",
        "apple_pay",
        "google_pay",
        "gift_card",
        "crypto",
    ]

    def __init__(self, data_type: str = "json"):
        self.data_type = data_type

    def generate(self):
        self.transaction_id = f"tx{get_id()}"
        self.user_id = f"u{get_id()}"
        self.timestamp = get_time().strftime("%Y-%m-%dT%H:%M:%SZ")

        import random

        self.amount = random.randint(1000, 10000000)
        self.currency = "KRW"
        self.method = random.choice(self.methods)
        self.status = random.choice(["success", "failed"])

    def get_data(self):
        return {
            "transaction_id": self.transaction_id,
            "user_id": self.user_id,
            "amount": self.amount,
            "currency": self.currency,
            "method": self.method,
            "status": self.status,
            "timestamp": self.timestamp,
        }

    def to_text(self):
        return f"[{self.timestamp}] {self.user_id} {self.transaction_id} {self.amount}{self.currency} via {self.method} -> {self.status}"
