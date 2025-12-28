import json
import joblib
import mysql.connector
from kafka import KafkaConsumer


model = joblib.load("model/fraud_model.pkl")

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MOHmoh**##2418", 
    database="payment_scoring"
)
cursor = db.cursor()


consumer = KafkaConsumer(
    'payments',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Consumer is running... waiting for transactions.")

for msg in consumer:
    transaction = msg.value
    print("Received:", transaction)

    amount = transaction['amount']
    score = model.predict_proba([[amount]])[0][1]
    is_fraud = score > 0.5

    if not is_fraud:
        print("Legal")
    else:
        print("Fraud")

    insert_query = """
    INSERT INTO scored_transactions (transaction_id, user_id, amount, score, is_fraud)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, (
        transaction['transaction_id'],
        transaction['user_id'],
        amount,
        score,
        int(is_fraud)  # 0 = legal, 1 = fraud
    ))
    db.commit()
    print("Saved to MySQL\n")
