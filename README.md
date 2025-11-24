#  Velib Use case

Prepared by:

Wiam LACHQER

Ossama OUALY

This project was completed as part of the Data Stream Processing course in the M2 Data Science program at École Polytechnique.

This project implements a full end-to-end real-time data processing pipeline using the JCDecaux Velib API and Apache Kafka.

##  Project Structure

kafka_LAB/
│
├── ingest-data.py
├── stations-activity.py
├── empty-stations.py
├── alert-empty-stations.py
├── archive-data.py
├── monitor-kafka.py
│
└── README.md


## The Environment
=> Start ZooKeeper
cd kafka_2.13-3.x.x
bin/zookeeper-server-start.sh config/zookeeper.properties

=> Start the Kafka Broker
bin/kafka-server-start.sh config/server.properties

=> Create the Kafka topics required for the lab
bin/kafka-topics.sh --create --topic velib-stations --bootstrap-server localhost:9092
bin/kafka-topics.sh --create --topic stations-status --bootstrap-server localhost:9092
bin/kafka-topics.sh --create --topic empty-stations --bootstrap-server localhost:9092