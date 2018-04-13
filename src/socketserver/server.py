#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import socket
from utils.log import get_logger
log = get_logger("Server")


class Server(threading.Thread):
    """
    Socket echo server that sends received message back to the client.
    """

    def __init__(self, address, port):
        super(Server, self).__init__()
        self.address = address or "127.0.0.1"
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def listen(self):
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)
        log.debug("Listening on %s" % str((self.address, self.port)))

    def start_listening(self):
        self.listen()
        try:
            client_socket, client_address = self.socket.accept()
            log.debug("Client connected: %s" % str(client_address))
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                log.debug("Received message: %s" % data)
                client_socket.sendall(data)
                log.debug("Echo message: %s" % data)
            client_socket.close()
        except:
            raise

    def run(self):
        self.start_listening()

    def join(self, timeout=None):
        super(Server, self).join(timeout)
        self.socket.close()
        log.debug("%s has stopped listening" % str((self.address, self.port)))
