# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

bind = '0.0.0.0:5005'
import multiprocessing
workers = multiprocessing.cpu_count() * 2 + 1
accesslog = '-'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
