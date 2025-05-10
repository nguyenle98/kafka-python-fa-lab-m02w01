from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic_name = 'Purchase'
producer.send(topic_name, b'Test message from producer')
producer.flush()
