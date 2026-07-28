import pika

# Callback function to handle received messages
def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")

# Establish a connection to RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost')
)

channel = connection.channel()

# Declare the same queue 'hello' as the producer
channel.queue_declare(queue='hello' , durable=True)

# Setup a callback function to handle incoming messages
channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print("[*] Waiting for messages. To exit, press Ctrl+C")

# Start consuming messages from the 'hello' queue
channel.start_consuming()