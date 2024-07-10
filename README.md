# Real-Time Streaming Data Pipeline with Kafka and Docker
## Overview
    - The goal of this project is to construct a real-time streaming data pipeline that uses Docker and Kafka to ingest, process, and store streaming data. The pipeline consists of parts for reading messages from a Kafka topic, analyzing the information, and creating messages and insights for new topics in Kafka

## Components
    - Kafka: Message broker for streaming data.
    - Zookeeper: Coordination service for Kafka.
    - Python Kafka Consumer and Producer: Processes the data and generates insights.
    - Docker Compose: Manages the deployment of Kafka, Zookeeper, and the data generator.

## Setup Instructions
### Prerequisites
    - Docker and Docker Compose installed on your machine.
### Steps
    - Git clone https://github.com/VidyaranyaRJ/Real-time-Streaming-Data-Pipeline-with-Kafka.git
    - Create a docker-compose.yml
    - Start Docker Containers: docker-compose up -d
    - Verify Kafka Topics: docker exec -it <kafka-container-id> kafka-topics --list --bootstrap-server localhost:9092
## Kafka Consumer and Producer
### Kafka Consumer
    - The Kafka consumer listens to the user-login topic, deserializes incoming messages, and processes the data.
### Kafka Producer
    - The Kafka producer sends processed data and insights to new Kafka topics (processed-user-login and user-login-insights).
=======
# Real-Time Streaming Data Pipeline with Kafka and Docker
## Overview
    - The goal of this project is to construct a real-time streaming data pipeline that uses Docker and Kafka to ingest, process, and store streaming data. The pipeline consists of parts for reading messages from a Kafka topic, analyzing the information, and creating messages and insights for new topics in Kafka

## Components
    - Kafka: Message broker for streaming data.
    - Zookeeper: Coordination service for Kafka.
    - Python Kafka Consumer and Producer: Processes the data and generates insights.
    - Docker Compose: Manages the deployment of Kafka, Zookeeper, and the data generator.

## Setup Instructions
### Prerequisites
    - Docker and Docker Compose installed on your machine.
### Steps
    - Git clone https://github.com/VidyaranyaRJ/Real-time-Streaming-Data-Pipeline-with-Kafka.git
    - Create a docker-compose.yml
    - Start Docker Containers: docker-compose up -d
    - Verify Kafka Topics: docker exec -it <kafka-container-id> kafka-topics --list --bootstrap-server localhost:9092
## Kafka Consumer and Producer
### Kafka Consumer
    - The Kafka consumer listens to the user-login topic, deserializes incoming messages, and processes the data.
### Kafka Producer
    - The Kafka producer sends processed data and insights to new Kafka topics (processed-user-login and user-login-insights).
>>>>>>> 2c2a511098b6884f073a7cfc69ad5cb4c90d895a
