#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging


def get_logger(name):
    log = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s:%(module)s(%(process)d): %(message)s"))
    log.addHandler(handler)
    log.setLevel(logging.INFO)
    return log
