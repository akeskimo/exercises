#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from log import get_logger
log = get_logger("Server")


class Server(object):
    """
    Socket server that will echo received message back to the client.
    """

    def __init__(self, address, port):
        self.address = address or "localhost"
        self.port = port

    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)

    def start_listening(self):
        self.listen()
        while True:
            try:
                client_socket, client_address = self.socket.accept()
                while True:
                    data = client_socket.recv(32)
                    if not data:
                        break
                    client_socket.sendall(data)
            except:
                raise

    def close(self):
        self.socket.close()
