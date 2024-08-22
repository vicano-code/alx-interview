#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""

import signal
import sys

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}
file_size = 0
counter = 0


def print_stats(file_size, status_codes):
    """prints the stats"""
    print(f"File size: {file_size}")
    for status, count in status_codes.items():
        if count > 0:
            print(f"{status}: {count}")


def signal_handler(sig, frame):
    """handle CtrlC keyboard interrupt"""
    print_stats(file_size, status_codes)


signal.signal(signal.SIGINT, signal_handler)

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
            status_codes[line_list[-2]] += 1
        except (ValueError, IndexError) as e:
            counter -= 1
    # print stats after every 10 lines
    if counter % 10 == 0:
        print_stats(file_size, status_codes)
