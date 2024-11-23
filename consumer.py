import pika
from pprint import pprint
def callback(ch,method,properties,body):
    message = body.decode()
    print('message:', message)
    pprint({'ch': ch, 'method': method, 'body': body, 'properties': properties})

params = pika.URLParameters('amqps://zrblewkb:KzbMzfD3OG2RP5k-Q85ACcGNhK12HtyU@puffin.rmq2.cloudamqp.com/zrblewkb')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='my_queue')
channel.basic_consume(
    queue='my_queue',
    on_message_callback=callback,
    auto_ack=True
)
print('Consumer is Ready for the queue!')
channel.start_consuming()