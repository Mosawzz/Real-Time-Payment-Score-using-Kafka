# Real-Time Payment Score System ⚡💳

A real-time payment risk scoring system that evaluates financial transactions instantly using **Apache Kafka** and **Machine Learning**.  
The system is designed to mimic real-world financial pipelines where low latency and scalability are critical.

---

## 🚀 Project Summary (Recruiter-Friendly)

- Built a **real-time streaming system** for payment transaction scoring  
- Implemented **Apache Kafka using Java** for high-throughput event streaming  
- Applied **Machine Learning** to generate instant payment risk scores  
- Designed the system with scalability and real-world financial use cases in mind  

---

## 🏗️ System Architecture
[ Payment Generator ]
|
v
[ Java Kafka Producer ]
|
v
[ Apache Kafka Topic ]
|
v
[ Kafka Consumer ]
|
v
[ ML Scoring Engine ]
|
v
[ Real-Time Risk Score Output ]

---

## 🧠 How It Works

1. Payment transactions are generated in real time.
2. A **Kafka Producer written in Java** publishes transactions to Kafka topics.
3. Kafka streams transactions reliably and efficiently.
4. A Kafka Consumer processes incoming data.
5. The ML model evaluates each transaction and outputs a **risk score** instantly.

---

## 🛠️ Technologies Used

- **Java** – Kafka Producer implementation  
- **Apache Kafka** – Real-time data streaming  
- **Python** – Data preprocessing & ML inference  
- **Scikit-learn** – Machine learning model  
- **NumPy / Pandas** – Feature engineering  

---

## ⚙️ Kafka Implementation Details

- Apache Kafka was configured and run locally.
- Topics were created to stream payment transactions.
- A **Java-based Kafka Producer** sends payment events in real time.
- Consumers subscribe to Kafka topics and process data with minimal latency.

---

## ▶️ How to Run

### 1️⃣ Start Kafka & Zookeeper
```bash
zookeeper-server-start.sh config/zookeeper.properties
kafka-server-start.sh config/server.properties
```
## ▶️ How to Run

### 2️⃣ Create Kafka Topic
```bash
kafka-topics.sh --create \
  --topic payments \
  --bootstrap-server localhost:9092 \
  --partitions 1 \
  --replication-factor 1
```
### 3️⃣ Run Java Kafka Producer

  Starts streaming payment transactions to Kafka in real time.

### 4️⃣ Run Consumer & ML Scoring

  Consumes transactions from Kafka
  
  Applies data preprocessing
  
  Outputs payment risk score instantly

### 📊 Use Cases

  Real-time fraud detection
  
  Payment risk assessment
  
  Credit scoring systems
  
  Financial transaction monitoring

### 🔮 Future Enhancements

  Deep learning–based scoring models
  
  Real-time dashboard (Grafana / Streamlit)
  
  Database integration (PostgreSQL / MongoDB)
  
  Docker & Kubernetes deployment

----

## 👤 Author

**Mohamed Ezzat Mostafa**  

AI Student – Faculty of Computers and Artificial Intelligence, Helwan University  

### Links
- GitHub: https://github.com/Mosawzz  
- Kaggle: https://www.kaggle.com/ezzatt  
- LinkedIn: https://www.linkedin.com/in/mohamed-ezzat-8b3783258/
