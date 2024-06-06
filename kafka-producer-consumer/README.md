# Kafka Producer and Consumer

This project contains simple producer and consumer programs for Apache Kafka written in Python, along with Docker configurations to easily set up Kafka and Zookeeper services.

## Getting Started

### Prerequisites

- Python 3.x
- Docker
- Docker Compose

### Installing

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Sowrabhm1931/learning-projects.git
   cd learning-projects
   ```

2. **Install Python Dependencies**

   ```bash
   pip install confluent_kafka
   ```

3. **Ensure Docker and Docker Compose are Installed**

   You can install Docker and Docker Compose by following the instructions [here](https://docs.docker.com/get-docker/) and [here](https://docs.docker.com/compose/install/).

### Setting Up Kafka and Zookeeper with Docker

1. **Start Kafka and Zookeeper Services**

   ```bash
   docker-compose up -d
   ```

   This will pull the necessary Docker images and start the Kafka and Zookeeper services as defined in the `docker-compose.yml` file.

2. **Verify the Services are Running**

   ```bash
   docker-compose ps
   ```

   You should see `kafka`, `zookeeper`, `producer`, and `consumer` services listed.

### Running the Producer

1. **Edit `producer.py`**

   Ensure the Kafka broker address is set correctly:

   ```python
   conf = {'bootstrap.servers': "localhost:39092"}
   ```

2. **Run the Producer**

   ```bash
   python producer.py
   ```

   Enter a message when prompted. Type `exit` to quit the producer.

### Running the Consumer

1. **Edit `consumer.py`**

   Ensure the Kafka broker address and topic are set correctly:

   ```python
   conf = {
       'bootstrap.servers': "localhost:39092",
       'group.id': "orders-group",
       'auto.offset.reset': 'earliest'
   }
   ```

2. **Run the Consumer**

   ```bash
   python consumer.py
   ```

   The consumer will continuously listen for messages on the specified topic.

### Docker Configuration

#### Dockerfile for Producer

```dockerfile
# Dockerfile-producer
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run producer.py when the container launches
CMD ["python", "producer.py"]
```

#### Dockerfile for Consumer

```dockerfile
# Dockerfile-consumer
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run consumer.py when the container launches
CMD ["python", "consumer.py"]
```

#### Docker Compose Configuration

```yaml
# docker-compose.yml
version: '3'
services:
  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    environment:
      ZOOKEEPER_CLIENT_PORT: 32181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - "32181:2181"

  kafka:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:32181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:39092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
    ports:
      - "39092:9092"

  producer:
    build:
      context: .
      dockerfile: Dockerfile-producer
    depends_on:
      - kafka
    environment:
      - KAFKA_BOOTSTRAP_SERVERS=kafka:9092
    stdin_open: true
    tty: true

  consumer:
    build:
      context: .
      dockerfile: Dockerfile-consumer
    depends_on:
      - kafka
    environment:
      - KAFKA_BOOTSTRAP_SERVERS=kafka:9092
```

### License

This project is licensed under the MIT License.
```

In this README.md:

- **Prerequisites** section lists all necessary installations.
- **Installing** section provides instructions to clone the repository and install dependencies.
- **Setting Up Kafka and Zookeeper with Docker** section guides users to start services with Docker Compose.
- **Running the Producer** and **Running the Consumer** sections explain how to run the producer and consumer scripts.
- **Docker Configuration** section includes the full content of the Dockerfiles and `docker-compose.yml`, clearly labeled and separated.