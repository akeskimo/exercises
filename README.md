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

The socket server has client and server implementation, but there is a design
flaw that causes the socketserver test to deadlock.

Q1: Why does the test hang?

Q2: How would you modify tests and/or the implementation so that multiple clients can connect to the server?

Q3: Can you make the server to support multiple client connections simultaneously and write a test for it?


# Exercise 2 - multithread

This program has a thread pool that encrypts data to a file in one
thread and decrypts the file's contents in another thread, but the
data gets corrupted. Can you fix the program?

$ src/multithread/encryption.py


# Handover

After you have completed the exercises, you can send
the result back as tar.gz (eg. git-archive).


# Help

If you face problems or come up with questions, you may contact
aapokesk@gmail.com.
