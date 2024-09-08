# Streaming--data-engineering-project
This project creates a robust data pipeline for efficient ingestion, processing, and storage. Using Apache Airflow for orchestration, it integrates Python, Kafka, Zookeeper, and Spark for real-time data processing, with Cassandra for storage. Docker containerization ensures smooth deployment and scalability of all components.

# Realtime Data Streaming | End-to-End Data Engineering Project

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [What I Learned](#what-i-learned)
- [Technologies](#technologies)

## Introduction

I recently completed an end-to-end data engineering pipeline project, where I built a system that handles data ingestion, processing, and storage. For this, I used a range of technologies including Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. To ensure smooth deployment and scalability, I containerized everything with Docker.

## System Architecture

![System Architecture](https://github.com/airscholar/e2e-data-engineering/blob/main/Data%20engineering%20architecture.png)

The architecture I implemented consists of several components:

- **Data Source**: I used the `randomuser.me` API to generate random user data for the pipeline.
- **Apache Airflow**: This orchestrates the pipeline, starting with fetching data and storing it in PostgreSQL.
- **Apache Kafka and Zookeeper**: These handle real-time data streaming from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: These help monitor Kafka streams and manage schemas.
- **Apache Spark**: This processes the data using Spark’s distributed computing capabilities.
- **Cassandra**: Stores the processed data for further analysis.

## What I Learned

- How to set up and orchestrate a data pipeline using Apache Airflow.
- Implementing real-time data streaming with Apache Kafka.
- How Zookeeper enables distributed synchronization in a pipeline.
- Data processing with Apache Spark’s cluster model.
- Storing processed data in Cassandra and PostgreSQL.
- The value of containerizing with Docker for deployment and scalability.

## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

