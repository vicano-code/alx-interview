#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""

import signal
import sys

status_code = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}
file_size = 0
counter = 0

# read line from stdin
for line in sys.stdin:
    counter += 1
    
    # strip spaces before and after line
    line = line.strip()
    # split line into words based on whitespace
    line_list = line.split()

    # check line_list to ensure it meets the required size or format
    if len(line_list) == 9:
        try:
            # cummulate file size after each valid line
            file_size += int(line_list[-1])

            # increment status code count
            status_code[line_list[-2]] += 1
        except Exception:
            counter -= 1
            pass
    # print stats after every 10 lines
    if counter % 10 == 0:
        print(f"File size: {file_size}")
        for key, val in status_code.items():
            if val != 0:
                print(f"{key}: {val}")
