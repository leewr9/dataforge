from stream.base import StreamWrapper
from kafka import KafkaProducer
import json


class KafkaProducerWrapper(StreamWrapper):
    def __init__(self, host="localhost", port=9092):
        self.producer = None

        if not self._check_connection(host, port):
            raise ConnectionError(f"Cannot connect to Kafka at {host}:{port}")

        try:
            self.producer = KafkaProducer(bootstrap_servers=f"{host}:{port}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Kafka at {host}:{port}: {e}")

    def send(self, topic: str, message: str | dict):
        if not self.producer:
            raise RuntimeError("Kafka producer not initialized. Cannot send message.")

        try:
            if isinstance(message, dict):
                message = json.dumps(message)
            self.producer.send(topic, value=message.encode("utf-8"))
            self.producer.flush()
        except Exception as e:
            raise RuntimeError(f"Failed to send message to topic '{topic}': {e}")

    def close(self):
        if self.producer:
            try:
                self.producer.flush()
                self.producer.close()
            except Exception as e:
                raise RuntimeError(f"Failed to close Kafka producer properly: {e}")
