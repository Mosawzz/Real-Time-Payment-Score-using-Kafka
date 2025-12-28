from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transactions = [
    {"transaction_id": "tx1", "user_id": "u1", "amount": 250},
    {"transaction_id": "tx2", "user_id": "u2", "amount": 300},
    {"transaction_id": "tx3", "user_id": "u3", "amount": 50},
    {"transaction_id": "tx4", "user_id": "u4", "amount": 1200},
]

for txn in transactions:
    producer.send('payments', txn)
    print(f"Sent: {txn}")
    time.sleep(1)  

producer.flush()
producer.close()
