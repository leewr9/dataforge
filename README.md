# Dataforge

Generate diverse raw data from different events, logs, and interactions, and output it in any format you need. With support for a wide range of test data, you can explore and use it freely.

## Feature

- Generate diverse raw data across multiple domains.
- Supports various output formats: `Text`, `JSON`, `CSV`
- Stream data directly to messaging platforms.
- Control data generation flexibly via line count or duration.
- Extend easily with modular data classes for custom data types.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/leewr9/dataforge.git
   cd dataforge
   ```

2. **Install dependencies via uv**

   ```bash
   uv sync
   ```

## Usage

You can specify the **Output type**, the **Data domain** and additional configuration options.

```bash
uv run python main.py [options]
```

### Options

| Option                     | Description                                                             | Default           |
| -------------------------- | ----------------------------------------------------------------------- | ----------------- |
| `-t`, `--type`             | Output type: `file` or `stream`                                         | _required_      |
| `-d`, `--data`             | Data domain: `access`, `clickstream`, `iot`, `payments`, `security`     | _required_      |
| `-l`, `--line`             | Number of lines to generate (if not set, uses `--duration`)             | `None`            |
| `-du`, `--duration`        | Duration in seconds to generate data (ignored if `--line` is specified) | `300` (5 minutes) |
| `-df`, `--data-format`     | Data format: `json`, `csv`, `text`                                      | `json`            |
| `-sp`, `--stream-platform` | Streaming platform: `kafka`, `pulsar`                                   | `kafka`           |
| `-tp`, `--topic`           | Topic name for streaming output                                         | `test`            |

### Examples

- **Generate file data**
  - Generate `access` events of **1000 records** as `JSON`:
    ```bash
    uv run python main.py -t file -d access -l 1000 -ff json
    ```
  - Generate `clickstream` events for **10 minutes** as `CSV`:
    ```bash
    uv run python main.py -t file -d clickstream -dr 600 -ff csv
    ```

- **Stream data to Kafka**
  - Send `payment` events continuously to `Kafka`:
    ```bash
    uv run python main.py -t stream -d payment -sp kafka --topic payments
    ```

- **Stream data to Pulsar**
  - Send `iot` events for **1 hour** to `Pulsar`:
    ```bash
    uv run python main.py -t stream -d iot -dr 3600 -sp pulsar --topic iots
    ```

### Help

For detailed usage, run:

```bash
uv run python main.py --help
```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
