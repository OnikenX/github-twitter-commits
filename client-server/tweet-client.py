#!/bin/python
#OnikenX#
# Save as client.py
import socket

HEADER = 64
PORT = 5050
SERVER = "192.168.1.10"
ADDR = (SERVER, PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False

def close():
    send(DISCONNECT_MESSAGE)
    client.close()

while connected == False:
    try:    
        client.connect(ADDR)
        connected = True
    except:
        try:
            SERVER = input(f'Error connecting to {SERVER}, try new adress or ^D to exit:')
        except:
            exit(3)
    

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

try:
    INPUT = input('Tweet: ')
except:
    close()

send(INPUT)
close()
