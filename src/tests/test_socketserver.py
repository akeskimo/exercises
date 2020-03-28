#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import testlib

import unittest
from socketserver.server import Server
from socketserver.client import Client


class TestServer(unittest.TestCase):
    address = ""
    port = 9090
    server = None

    @classmethod
    def setUp(self):
        self.server = Server(self.address, self.port)
        self.server.start()

    @classmethod
    def tearDown(self):
        self.server.join()
        self.server = None

    def test_write_read_message(self):
        """ Send message to server and verify reply. """
        message = b"Let the Open-Source be with you"
        client = Client(self.address, self.port)
        client.connect()
        client.send(message)
        received = client.receive()
        client.close()
        self.assertEqual(message, received)

    def test_write_read_message_with_multiple_clients(self):
        """ Send message to a server from multiple clients and verify replies. """

        # TODO What went wrong with this test? How would you modify the tests / classes so that it would work as expected?

        fmt = b"Client %d says hello"
        clients = [(Client(self.address, self.port), fmt % i) for i in range(5)]
        for (client, message) in clients:
            client.connect()
            client.send(message)
            received = client.receive()
            client.close()
            self.assertEqual(message, received)


if __name__ == '__main__':
    unittest.main(verbosity=2)
