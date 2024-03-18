# import pika,json
# conn=pika.BlockingConnection(pika.ConnectionParameters(host='192.168.68.76'))
# channel=conn.channel()

# def publish(method,body):
#     channel.basic_publish(exchange='',routing_key='main',body=json.dumps(body))
