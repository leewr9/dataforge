import json
import random
import time
from data.base import BaseData


def file(data: BaseData, lines=None, duration=300):
    with open(data.get_filename(), "a", encoding="utf-8") as f:
        if lines:
            f.write(data.get(header=True) + "\n")
            for _ in range(lines - 1):
                f.write(data.get() + "\n")
        else:
            end_time = time.time() + duration
            f.write(data.get(header=True) + "\n")
            while time.time() < end_time:
                f.write(data.get() + "\n")
                f.flush()
                time.sleep(random.uniform(0.1, 1.0))


def stream(
    data: BaseData,
    topic: str,
    lines=None,
    duration=300,
    stream_type="kafka",
    stream_url=None,
):
    from stream.kafka import KafkaProducerWrapper
    from stream.pulsar import PulsarProducerWrapper

    if not stream_url:
        if stream_type == "kafka":
            stream_url = "localhost:9092"
        elif stream_type == "pulsar":
            stream_url = "localhost:6650"
    host, port = stream_url.rsplit(":", 1)

    if stream_type == "kafka":
        producer = KafkaProducerWrapper(host, port)
    elif stream_type == "pulsar":
        producer = PulsarProducerWrapper(host, port)
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
