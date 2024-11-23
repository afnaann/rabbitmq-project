import pika



def publish_message(message):
    params = pika.URLParameters('amqps://zrblewkb:KzbMzfD3OG2RP5k-Q85ACcGNhK12HtyU@puffin.rmq2.cloudamqp.com/zrblewkb')
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue='my_queue')
    channel.basic_publish(exchange='',
                          routing_key='my_queue',
                          body=message)
    channel.close()