from data.base import BaseData
from data.utils import get_time, get_id, get_ip


class SecurityData(BaseData):
    name = "security"
    events = [
        "login_success",
        "login_failed",
        "brute_force",
        "session_timeout",
        "password_change",
        "account_lock",
        "mfa_enabled",
        "mfa_failed",
        "unauthorized_access",
        "file_download",
        "file_upload",
        "vpn_connect",
        "vpn_disconnect",
        "privilege_escalation",
    ]

    def __init__(self, data_type: str = "json"):
        self.data_type = data_type

    def generate(self):
        self.user_id = f"u{get_id()}"
        self.ip = get_ip()
        self.timestamp = get_time().strftime("%Y-%m-%dT%H:%M:%SZ")

        import random

        self.event = random.choice(self.events)

    def get_data(self):
        return {
            "user_id": self.user_id,
            "ip": self.ip,
            "event": self.event,
            "timestamp": self.timestamp,
        }

    def to_text(self):
        return f'[{self.timestamp}] "{self.user_id}"@{self.ip} -> {self.event}'
