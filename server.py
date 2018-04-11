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
        self.address = address or "127.0.0.1"
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)

    def start_listening(self):
        self.listen()
        log.info("Started listening on %s." % (str((self.address, self.port))))
        try:
            client_socket, client_address = self.socket.accept()
            log.info("Received connection %s." % str(client_address))
            while True:
                data = client_socket.recv(32)
                if not data:
                    break
                client_socket.sendall(data)
            client_socket.close()
        except:
            raise

    def close(self):
        self.socket.close()
