import requests
import time
import random

url = "http://127.0.0.1:5000/api/data"

print("--- Simulator Started ---")
while True:
    payload = {
        "sensor_id": "ESP32_MOROCCO_01",
        "moisture": round(random.uniform(20.0, 80.0), 1),
        "temperature": round(random.uniform(15.0, 35.0), 1),
        "humidity": random.randint(30, 90)
    }
    
    try:
        response = requests.post(url, json=payload)
        print(f"Sent: {payload['moisture']}% moisture | Status: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(3) # Ssifet data kola 3 swaye3