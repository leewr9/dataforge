import argparse
from data.access import AccessData
from data.clickstream import ClickstreamData
from data.iot import IoTData
from data.payment import PaymentsData
from data.security import SecurityData
from generator import file as file_write, stream as stream_send

DATA_TYPES = {
    "access": AccessData,
    "clickstream": ClickstreamData,
    "iot": IoTData,
    "payments": PaymentsData,
    "security": SecurityData,
}


def main():
    parser = argparse.ArgumentParser(
        description=(
            "DataForge: Generate diverse raw data from events, logs, and interactions.\n"
            "Output data in any format you need. Supports a wide range of test datasets."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "--type",
        "-t",
        required=True,
        choices=["file", "stream"],
        help="Output method: 'file' to save locally, 'stream' to send to a streaming platform",
    )

    parser.add_argument(
        "--data",
        "-d",
        required=True,
        choices=DATA_TYPES.keys(),
        help="Data type to generate (e.g., clickstream, iot, payments, security, access, game)",
    )

    parser.add_argument(
        "--lines",
        "-l",
        type=int,
        default=None,
        help="Number of data entries to generate. If omitted, duration is used.",
    )

    parser.add_argument(
        "--duration",
        "-du",
        type=int,
        default=300,
        help="Duration in seconds to generate data when --lines is not specified",
    )

    parser.add_argument(
        "--file-format",
        "-ff",
        choices=["text", "json", "csv"],
        default="json",
        help="File format to save data (applies only when --type is 'file')",
    )

    parser.add_argument(
        "--stream-platform",
        "-sp",
        choices=["kafka", "pulsar"],
        default="kafka",
        help="Streaming platform to send data (applies only when --type is 'stream')",
    )

    parser.add_argument(
        "--topic",
        "-tp",
        default="test",
        help="Topic name for streaming platform (applies only when --type is 'stream')",
    )

    args = parser.parse_args()

    if args.type == "file":
        file_write(
            DATA_TYPES[args.data],
            lines=args.lines,
            duration=args.duration,
            file_type=args.file_format,
        )
    if args.type == "stream":
        stream_send(
            DATA_TYPES[args.data],
            topic=args.topic,
            lines=args.lines,
            duration=args.duration,
            stream_type=args.stream_platform,
        )


if __name__ == "__main__":
    main()
