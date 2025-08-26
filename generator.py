import json
import random
import time
from data.base import BaseData


def file(data_cls: BaseData, lines=None, duration=300, file_type="json"):
    data = data_cls(file_type)

    with open(data.get_filename(), "a", encoding="utf-8") as f:
        if lines:
            for _ in range(lines):
                f.write(data.get() + "\n")
        else:
            end_time = time.time() + duration
            while time.time() < end_time:
                f.write(data.get() + "\n")
                f.flush()
                time.sleep(random.uniform(0.1, 1.0))


def stream(
    data_cls: BaseData, topic: str, lines=None, duration=300, stream_type="kafka"
):
    data = data_cls("json")

    from stream.kafka import KafkaProducerWrapper
    from stream.pulsar import PulsarProducerWrapper

    if stream_type == "kafka":
        producer = KafkaProducerWrapper()
    elif stream_type == "pulsar":
        producer = PulsarProducerWrapper()
    else:
        raise ValueError(f"Unsupported stream type: {stream_type}")

    if lines:
        for _ in range(lines):
            producer.send(topic, data.get())
    else:
        end_time = time.time() + duration
        while time.time() < end_time:
            producer.send(topic, data.get())
            time.sleep(random.uniform(0.1, 1.0))

    producer.close()
