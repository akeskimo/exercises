# Python Exercise


# About This Repository

This repository contains python puzzles for exercising programming
skills. Follow the instructions below and try to solve the problems.


# Install

1. If you do not have python3.6+, you may download it from official page

   https://www.python.org/downloads/

2. Configure project

   $ make install

3. Activate virtual environment

   $ . env/bin/activate


# Exercise 1 - socketserver

The socket server has client and server implementation in the source
folder, but there is a design flaw in the server. In order to help
debugging the problem, you may execute unit tests and possibly
find out a solution to fix it:

$ src/tests/test_socketserver.py


# Exercise 2 - multithread

This program has a thread pool that encrypts data to a file in one
thread and decrypts the file's contents in another thread, but the
data gets corrupted. Can you fix the program?

$ src/multithread/encryption.py


# Handover

After you have completed the exercises, it is recommended to send
them back in tar.gz format.


# Help

If you face problems or come up with questions, you may contact
aapo.keskimolo@qt.io.
