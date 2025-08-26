from stream.base import StreamWrapper
from pulsar import Client
import json
import socket


class PulsarProducerWrapper(StreamWrapper):
    def __init__(self, host="localhost", port=6650):
        self.client = None
        self.producers = {}

        if not self._check_connection(host, port):
            raise ConnectionError(f"Cannot connect to Pulsar at {host}:{port}")

        try:
            self.client = Client(f"pulsar://{host}:{port}")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Pulsar at {host}:{port}: {e}")

    def send(self, topic: str, message: str | dict):
        if not self.client:
            raise RuntimeError("Pulsar client not initialized. Cannot send message.")

        try:
            if isinstance(message, dict):
                message = json.dumps(message)

            if topic not in self.producers:
                self.producers[topic] = self.client.create_producer(topic)

            self.producers[topic].send(message.encode("utf-8"))
            self.producers[topic].flush()
        except Exception as e:
            raise RuntimeError(f"Failed to send message to topic '{topic}': {e}")

    def close(self):
        if self.client:
            try:
                for producer in self.producers.values():
                    producer.close()
                self.client.close()
            except Exception as e:
                raise RuntimeError(f"Failed to close Pulsar client properly: {e}")
