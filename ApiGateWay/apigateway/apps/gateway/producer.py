import pika,json



def publish(method, body):
    RABBITMQ_HOST = 'rabbitmq'
    RABBITMQ_PORT = 5672
    conn = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT))
    channel = conn.channel()
    channel.queue_declare(queue='main')
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body))
    conn.close()