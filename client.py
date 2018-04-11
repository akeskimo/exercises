#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from time import sleep
import socket
from log import get_logger
log = get_logger("Client")


class Client:
    def __init__(self, host, port):
        self._host = host or "localhost"
        self._port = port
        self.__message_length = 0

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for retry in range(3, 1, -1):
            try:
                self.socket.connect((self._host, self._port))
                log.info("Connected to server %s:%s." % (self._host, self._port))
                return
            except ConnectionRefusedError:
                log.info("Retrying connection... Attempts left: %s", retry-1)
                sleep(1)
        raise ConnectionRefusedError("Unable to connect to server")

    def close(self):
        self.socket.close()

    def send(self, message):
        self.socket.sendall(message)
        self.__message_length = len(message)
        log.info("Sent: %s" % message)

    def receive(self):
        data = b""
        rcvd_len = 0
        while rcvd_len < self.__message_length:
            try:
                recvd = self.socket.recv(32)
                if not recvd:
                    break
                data += recvd
                rcvd_len += len(data)
            except ConnectionResetError:
                log.info("Connection reset.")
                break
        self.__message_length = 0
        return data


if __name__ == "__main__":
    client = Client("", 9999)
    try:
        client.connect()
        i = 0
        import time
        while True:
            i += 1
            msg = bytes(str(i).encode("utf-8"))
            client.send(msg)
            client.receive()
            time.sleep(1)
    except BrokenPipeError:
        log.info("Server refused connection.")
        client.close()
    finally:
        client.close()
