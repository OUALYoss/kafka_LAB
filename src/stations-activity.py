from confluent_kafka import Consumer, Producer
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Kafka configuration
BOOTSTRAP_SERVERS = 'localhost:9092'
INPUT_TOPIC = 'velib-stations'
OUTPUT_TOPIC = 'stations-status'

# Dictionary to store the last known state of each station
# Key: station_number, Value: dict with available_bikes and available_bike_stands
station_states = {}

def create_consumer():
    """
    Create and return a Kafka consumer.
    Return : 
        A consumer
    """
    conf = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'group.id': 'stations-activity-group',
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True
    }
    consumer = Consumer(conf)
    consumer.subscribe([INPUT_TOPIC])
    logger.info(f"Consumer created for topic: {INPUT_TOPIC}")
    return consumer


def create_producer():
    """
    Create and return a Kafka producer.
    Return:
        A producer
    """
    conf = {
        'bootstrap.servers': BOOTSTRAP_SERVERS
    }
    producer = Producer(conf)
    logger.info(f"Producer created for topic: {OUTPUT_TOPIC}")
    return producer
