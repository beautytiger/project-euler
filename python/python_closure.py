#!/usr/bin/python
# -*- coding: utf-8 -*-


import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(1, 2)
sub_logger(2, 1)
