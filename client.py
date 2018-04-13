#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from time import sleep
from log import get_logger
log = get_logger("Client")


class Client:
    """
    Socket client that can connect to a server and send/receive data.
    """

    def __init__(self, host, port):
        self.host = host or "127.0.0.1"
        self.port = port
        self.msg_len = 0

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for retry in range(3, 1, -1):
            try:
                self.socket.connect((self.host, self.port))
                return
            except ConnectionRefusedError:
                sleep(1)
        raise ConnectionRefusedError("Unable to connect to server.")

    def send(self, message):
        self.socket.sendall(message)
        log.info("Sent to server: %s" % message)
        self.msg_len = len(message)

    def receive(self):
        data = b""
        length = 0
        while length < self.msg_len:
            try:
                recvd = self.socket.recv(1024)
                if not recvd:
                    break
                log.info("Received from server: %s" % recvd)
                data += recvd
                length += len(data)
            except:
                raise
        self.msg_len = 0
        return data

    def close(self):
        self.socket.close()
