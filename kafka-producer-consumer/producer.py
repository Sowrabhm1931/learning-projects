from confluent_kafka import Producer

conf = {'bootstrap.servers': "localhost:9092"}
producer = Producer(**conf)

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

while True:
    message = input("Enter a message to send (or type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    producer.produce('orders', value=message, callback=delivery_report)
    producer.flush()
