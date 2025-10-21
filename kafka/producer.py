from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))
products = ['Laptop','Phone','Headphones','Monitor']

while True:
    data = {"user_id": random.randint(1,1000), "product": random.choice(products), "price": random.randint(50,2000)}
    producer.send('clickstream', value=data)
    print(f"Sent: {data}")
    time.sleep(1)
