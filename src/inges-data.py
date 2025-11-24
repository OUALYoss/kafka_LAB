import json
import time
import requests
from confluent_kafka import Producer

# ENV VAR
API_KEY = "a40006d894b778be7036b588ce3fff23590c4b35"
TOPIC = "velib-stations"
URL = f"https://api.jcdecaux.com/vls/v1/stations?apiKey={API_KEY}"

# Kafka Producer
producer = Producer({'bootstrap.servers': 'localhost:9092'})

try:
    while True:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            stations = response.json()

            for station in stations:
                station_id = str(station.get("number"))  # ID unique 
                producer.produce(
                    TOPIC,
                    key=station_id,
                    value=json.dumps(station)
                )

            producer.flush()
            print(f"{len(stations)} stations sent to Kafka")
        else:
            print(f"Error API {response.status_code}: {response.text}")

        time.sleep(10)

except KeyboardInterrupt:
    print("Manual interruption")

except Exception as e:
    print(f"Error: {e}")

finally:
    producer.flush()