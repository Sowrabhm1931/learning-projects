# Kafka Producer and Consumer

This project contains simple producer and consumer programs for Apache Kafka written in Python.

## Getting Started

### Prerequisites

- Python 3.x
- Kafka-python library
- Apache Kafka

### Installing

1. Install the `confluent_kafka` library:

```bash
pip install confluent_kafka`
```

2. Ensure Apache Kafka and Zookeeper are running.

### Running the Producer

1. Edit `producer.py` to configure the Kafka broker and topic.
2. Run the producer:

    ```bash
    python producer.py
    ```

### Running the Consumer

1. Edit `consumer.py` to cofigure the Kafka broker, topic, and consumer group.
2. Run the consumer:

    ```bash
    python consumer.py
    ```

## License

This project is licensed under the MIT License.