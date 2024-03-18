# import pika,json,psycopg2

# conn=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel=conn.channel()
# channel.queue_declare(queue='main')

# def pg_connection():
#     """Postgres connection to database"""
#     try:
#         cnxn = psycopg2.connect(
#             host="localhost",
#             port=5432,
#             database="BookService",
#             user="postgres",
#             password="Admin!@7890")
#         return cnxn
#     except Exception as e:        
#         print("[Error] msg: ", str(e))   


    
# def executeQueryPG(query):
#     """Execute a query in Pg database"""
#     try:
#         pg_con =pg_connection()
#         cur = pg_con.cursor()
#         cur.execute(query)
#         cur.close()
#     except Exception as ex:
#         print(ex)
#         pg_con.rollback()



# def callback(ch,methos,properties,body):
#     data = json.loads(body)
#     for i in data :
#         query = f"""INSERT INTO public."Books" (title, authors, isbn, stock) VALUES ('{i.get('title')}', '{ i.get('authors')}', {i.get('isbn')}, {i.get('stock')})"""
#         print(query)
#         executeQueryPG(query)

# channel.basic_consume(queue='main',on_message_callback=callback,auto_ack=True)
# channel.start_consuming()

