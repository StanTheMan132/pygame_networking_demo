# The server side 
import socket
import logging
import time
import threading
import json

HOST = '127.0.0.1'
PORT = 1234

def thread_function(conn, addr):
    logging.info("Thread starting for client %s", addr)
    while True:
        data = conn.recv(32)
        print('recieved Data')
        s=json.dumps({'player': (200, 200)}).encode('utf-8')
        conn.sendall(s)
        print('sent data')
    print(data)
    logging.info("Thread %s: finishing", addr)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            client = threading.Thread(target=thread_function, args=(conn,addr))
            client.start()
