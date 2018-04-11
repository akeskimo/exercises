#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from server import Server
from client import Client
import threading


class ServerThread(threading.Thread):
    def __init__(self, address, port):
        super(ServerThread, self).__init__()
        self.server = Server(address, port)

    def run(self):
        super(ServerThread, self).__init__()
        self.server.start_listening()

    def join(self, timeout=None):
        self.server.close()


class TestServer(unittest.TestCase):
    address = ""
    port = 9090
    server_thread = None

    @classmethod
    def setUpClass(self):
        self.server_thread = ServerThread(self.address, self.port)
        self.server_thread.start()

    @classmethod
    def tearDownClass(self):
        self.server_thread.join()
        while self.server_thread.isAlive():
            pass
        self.server_thread = None

    def get_client(self):
        return Client(self.address, self.port)

    def test_write_read_data_on_server(self):
        """ Send message to server and read the response """
        message = b"hello server"
        client = self.get_client()
        client.connect()
        client.send(message)
        received = client.receive()
        client.close()
        self.assertEqual(message, received)


if __name__ == '__main__':
    unittest.main()
