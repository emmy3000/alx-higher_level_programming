#!/usr/bin/python3

"""
Module: ``101-stats.py``
"""

import sys

codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
        "405": 0, "500": 0}
total_size = 0
count = 0

try:
    for i, line in enumerate(sys.stdin, 1):
        split = line.split()
        if len(split) >= 3:
            if split[-2] in codes:
                codes[split[-2]] += 1
            total_size += int(split[-1])
            count += 1

        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in sorted(codes.items()):
                if value != 0:
                    print("{}:{}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in sorted(codes.items()):
        if value != 0:
            print("{}:{}".format(key, value))
