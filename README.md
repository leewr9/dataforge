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

| Option                     | Description                                                         | Default           |
| -------------------------- | ------------------------------------------------------------------- | ----------------- |
| `-t`, `--type`             | Output type: `file` or `stream`                                     | _required_        |
| `-d`, `--data`             | Data domain: `access`, `clickstream`, `iot`, `payments`, `security` | _required_        |
| `-l`, `--line`             | Number of lines to generate                                         | `None`            |
| `-du`, `--duration`        | Duration in seconds to generate data                                | `300` (5 minutes) |
| `-df`, `--data-format`     | Output data format: `text`, `json`, `csv`                           | `json`            |
| `-sp`, `--stream-platform` | Streaming platform: `kafka`, `pulsar`                               | `kafka`           |
| `-tp`, `--topic`           | Topic name for streaming output                                     | `test`            |

### Examples

- **Generate file data**
  - Generate `access` events of **1000 records** as `JSON`:
    ```bash
    uv run python main.py -t file -d access -l 1000 -ff json
    ```
  - Generate `clickstream` events for **10 minutes** as `CSV`:
    ```bash
    uv run python main.py -t file -d clickstream -du 600 -ff csv
    ```

- **Stream data to Kafka**
  - Send `payment` events continuously to `Kafka`:
    ```bash
    uv run python main.py -t stream -d payment -sp kafka --topic payments
    ```

- **Stream data to Pulsar**
  - Send `iot` events for **1 hour** to `Pulsar`:
    ```bash
    uv run python main.py -t stream -d iot -du 3600 -sp pulsar --topic iots
    ```

### Help

For detailed usage, run:

```bash
uv run python main.py --help
```

## Data Format

### Access

- **Text**

  ```plaintext
  [TIMESTAMP] [LOG_ID] [CLIENT_IP] [USER] [REQUEST] [STATUS] [BYTES_SENT] [REFERER] [DEVICE]
  ```

  > `[2025-08-27T13:00:00Z] access-123 192.168.1.10 "James Smith" "GET /home HTTP/1.1" 200 1024 "https://example.com" desktop`

- **JSON**
  ```json
  {
    "log_id": "access-123",
    "timestamp": "2025-08-27T13:00:00Z",
    "client_ip": "192.168.1.10",
    "user": "James Smith",
    "request": "GET /home HTTP/1.1",
    "status": 200,
    "bytes_sent": 1024,
    "referer": "https://example.com",
    "device": "desktop"
  }
  ```

### Clickstream

- **Text**
  ```plaintext
  [TIMESTAMP] [USER_ID] [DEVICE] [ACTION] [PAGE]
  ```
  > `[2025-08-27T13:00:00Z] u123 mobile page_view /home`
- **JSON**
  ```json
  {
    "user_id": "u123",
    "timestamp": "2025-08-27T13:00:00Z",
    "action": "page_view",
    "page": "/home",
    "device": "mobile"
  }
  ```

### Iot

- **Text**
  ```plaintext
  [TIMESTAMP] [DEVICE_ID] temp=[TEMPERATURE]°C hum=[HUMIDITY]% loc=[Location]
  ```
  > `[2025-08-27T13:00:00Z] sensor-123 temp=25.3°C hum=60% loc=37.1234, 127.5678`
- **JSON**
  ```json
  {
    "device_id": "sensor-123",
    "timestamp": "2025-08-27T13:00:00Z",
    "temperature": 25.3,
    "humidity": 60,
    "location": [37.1234, 127.5678]
  }
  ```

### Payment

- **Text**
  ```plaintext
  [TIMESTAMP] [USER_ID] [TRANSACTION_ID] [AMOUNT][CURRENCY] via [METHOD] -> [STATUS]
  ```
  > `[2025-08-27T13:00:00Z] u123 tx12345 1000KRW via credit_card -> success`
- **JSON**
  ```json
  {
    "transaction_id": "tx12345",
    "user_id": "u123",
    "amount": 1000,
    "currency": "KRW",
    "method": "credit_card",
    "status": "success",
    "timestamp": "2025-08-27T13:00:00Z"
  }
  ```

### Security

- **Text**
  ```plaintext
  [TIMESTAMP] [USER_ID]@[IP] -> [EVENT]
  ```
  > `[2025-08-27T13:00:00Z] u123@192.168.1.10 -> login_failed`
- **JSON**
  ```json
  {
    "user_id": "u123",
    "ip": "192.168.1.10",
    "event": "login_failed",
    "timestamp": "2025-08-27T13:00:00Z"
  }
  ```

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
