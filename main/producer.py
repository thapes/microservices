import pika, json

params = pika.URLParameters('amqps://qmxpmoar:Q8g9q5KVYTl5dI776J50IhE0HXwffIUV@cattle.rmq2.cloudamqp.com/qmxpmoar')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)