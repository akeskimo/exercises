#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
from log import get_logger

log = get_logger("Server")

class Server(object):
    """
    Simple server. The server will receive a message and echo it back to the client.
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
        log.info("Started listening on %s:%s." % (self.address, self.port))
        while True:
            try:
                log.info("Waiting for connection.")
                client_socket, client_address = self.socket.accept()
                log.info("Connection received from %s." % str(client_address))
                while True:
                    data = client_socket.recv(32)
                    if not data:
                        break
                    log.info("Received: %s" % data)
                    client_socket.sendall(data)
                    log.info("Echoed back to client.")
                log.info("Connection closed to %s." % str(client_address))
            except:
                raise

    def close(self):
        self.socket.close()
        log.info("Closed socket.")


if __name__ == "__main__":
    server = Server("", 9999)
    try:
        server.start_listening()
    except (KeyboardInterrupt, SystemExit):
        server.close()
    finally:
        server.close()
