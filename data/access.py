from data.base import BaseData
from data.utils import get_user, get_time, get_id, get_ip, get_page, get_device


class AccessData(BaseData):
    name = "access"
    methods = ["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"]

    status_codes = [200, 201, 301, 302, 400, 401, 403, 404, 500, 502, 503]
    status_weights = [60, 5, 3, 2, 5, 2, 1, 5, 3, 2, 2]
    referers = [
        "-",
        "https://google.com",
        "https://example.com",
        "/login",
        "/dashboard",
    ]

    def __init__(self, data_type: str = "json"):
        self.data_type = data_type

    def generate(self):
        self.log_id = f"access-{get_id()}"
        self.timestamp = get_time().strftime("%Y-%m-%dT%H:%M:%SZ")
        self.client_ip = get_ip()
        self.user = get_user()
        self.page = get_page()
        self.device = get_device()

        import random

        self.method = random.choice(self.methods)
        self.protocol = "HTTP/1.1"
        self.request = f"{self.method} {self.page} {self.protocol}"
        self.status = random.choices(
            self.status_codes, weights=self.status_weights, k=1
        )[0]
        self.bytes_sent = random.randint(200, 5000)
        self.referer = random.choice(self.referers)

    def get_data(self):
        return {
            "log_id": self.log_id,
            "timestamp": self.timestamp,
            "client_ip": self.client_ip,
            "user": self.user,
            "request": self.request,
            "status": self.status,
            "bytes_sent": self.bytes_sent,
            "referer": self.referer,
            "device": self.device,
        }

    def to_text(self):
        return f'[{self.timestamp}] {self.log_id} {self.client_ip} "{self.user}" "{self.request}" {self.status} {self.bytes_sent} "{self.referer}" {self.device}'
