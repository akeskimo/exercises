#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
import tempfile
import subprocess

crypto_exec = os.path.relpath(os.path.join(os.path.dirname(__file__), "../../", "bin/crypto"))

def wrapper(func, result, *args):
    """ Wrapper for saving result from thread. """
    result.append(func(*args))
    return result

def encrypt_data_to_file(filepath, data, passwd):
    """ Call cryptography module through subprocess to encode data. """
    cmd = [crypto_exec, "-mode encrypt", "-filepath %s" % filepath, "-password %s" % passwd, "-data '%s'" % data]
    output = subprocess.check_output(" ".join(cmd), shell=True).decode("utf-8")
    return output.rstrip("\n")

def decrypt_file(filepath, passwd):
    """ Read data from file (slow) """
    cmd = [crypto_exec, "-mode decrypt", "-filepath %s" % filepath, "-password %s" % passwd]
    output = subprocess.check_output(" ".join(cmd), shell=True).decode("utf-8")
    return output.rstrip("\n")

if __name__ == "__main__":
    """ This program calls binary file to encrypt and decrypt data. The operations are sequential and are in
    two different threads."""

    # TODO Try to fix the program so that the assert on last line passes without compromising performance.

    message = "I am so smart that sometimes I do not understand a single word of what I am saying."
    passwd = "guess"
    results = []
    loop = asyncio.get_event_loop()

    with tempfile.TemporaryDirectory(prefix="decrypt") as work_dir:
        with ThreadPoolExecutor(max_workers=10) as executor:
            for data in message.split(" "):
                filepath = tempfile.mktemp(dir=work_dir)
                loop.run_in_executor(
                    executor,
                    encrypt_data_to_file,
                    filepath,
                    data,
                    passwd)
                loop.run_in_executor(
                    executor,
                    wrapper,
                    decrypt_file,
                    results,
                    filepath,
                    passwd)
            output = " ".join(results)

    assert message == output, "%s does not match %s" % (message, output)
