from data.base import BaseData
from data.utils import get_time, get_id


class IoTData(BaseData):
    name = "iot"

    def __init__(self, data_type: str = "json"):
        self.data_type = data_type

    def generate(self):
        self.device_id = f"sensor-{get_id()}"
        self.timestamp = get_time().strftime("%Y-%m-%dT%H:%M:%SZ")

        import random

        self.temperature = round(random.uniform(20.0, 30.0), 2)
        self.humidity = round(random.uniform(40.0, 80.0), 2)
        self.location = [
            round(random.uniform(33.0, 43.0), 4),
            round(random.uniform(124.0, 132.0), 4),
        ]

    def get_data(self):
        return {
            "device_id": self.device_id,
            "timestamp": self.timestamp,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "location": self.location,
        }

    def to_text(self):
        return f"[{self.timestamp}] {self.device_id} temp={self.temperature}°C hum={self.humidity}% loc={self.location[0]},{self.location[1]}"
