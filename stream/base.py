from abc import ABC, abstractmethod
import socket


class StreamWrapper(ABC):
    def _check_connection(self, host: str, port: int, timeout=5) -> bool:
        try:
            with socket.create_connection((host, port), timeout):
                return True
        except Exception:
            return False

    @abstractmethod
    def send(self, topic: str, message: str):
        pass

    @abstractmethod
    def close(self):
        pass
