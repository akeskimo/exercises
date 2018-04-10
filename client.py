#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
log = logging.getLogger("Client")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)


class Client:

    def __init__(self, host, port):
        self.host = host or "localhost"
        self.port = port
        self.message_length = 0

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        log.info("Connected to server %s:%s." % (self.host, self.port))

    def close(self):
        self.socket.close()

    def send(self, message):
        self.socket.sendall(message)
        self.message_length = len(message)
        log.info("Sent: %s" % message)

    def receive(self):
        received_len = 0
        log.info("Received:")
        while received_len < self.message_length:
            try:
                data = self.socket.recv(32)
                if not data:
                    break
                received_len += len(data)
                log.info(data)
            except ConnectionResetError:
                log.info("Connection reset.")
                break
        self.message_length = 0


if __name__ == "__main__":
    client = Client("", 9999)
    try:
        client.connect()
        msg = b"Helloooo"
        client.send(msg)
        client.receive()
    finally:
        client.close()
