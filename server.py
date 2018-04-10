#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import logging
log = logging.getLogger("Server")
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

class Server(object):
    """
    Simple server application.
    """

    def __init__(self, address, port):
        self.address = address or "localhost"
        self.port = port

    def listen(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.address, self.port))
        self.socket.listen(1)

    def start(self):
        log.info("Started listening on %s:%s." % (self.address, self.port))
        self.listen()

        while True:
            log.info("Started waiting for connection.")
            self.socket.accept()
            try:
                client_socket, client_address = self.socket.accept()
                log.info("Connection received from %s." % str(client_address))
                while True:
                    data = client_socket.recv(32)
                    if not data:
                        break
                    log.info("Received: %s" % data)
                    client_socket.sendall(data)
                log.info("Connection closed to %s." % str(client_address))
            except:
                raise

    def stop(self):
        self.socket.close()


if __name__ == "__main__":
    server = Server("", 9999)
    try:
        server.start()
    except (KeyboardInterrupt, SystemExit):
        server.stop()
    finally:
        server.stop()
