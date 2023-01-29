"""
    This program sends a message to a queue on the RabbitMQ server.

    Author: Denise Case
    Date: January 14, 2023

    Modified by Chris Kollbaum, January 29, 2023

"""

# add imports at the beginning of the file
import pika

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
message = "This is a new message!"
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message) 
# print a message to the console for the user

print(f"[X] sent {message}")
# close the connection to the server
conn.close()
