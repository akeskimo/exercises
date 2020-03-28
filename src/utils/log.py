#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os


def get_logger(name):
    log = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s:%(module)s(%(process)d): %(message)s"))
    log.addHandler(handler)
    if os.environ.get("DEBUG"):
        log.setLevel(logging.DEBUG)
    return log
