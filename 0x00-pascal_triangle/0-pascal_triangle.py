#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
      returns a list of lists of integers representing the
      Pascal’s triangle of n
    """
    # validate input
    if not isinstance(n, int):
        raise TypeError(f"input must be an integer")
    if n <= 0:
        return []

    result = [[1]]
    next = [1]
    for j in range(n-1):
        tmp = [sum(next[i:i+2]) for i in range(len(next))]
        tmp.insert(0, 1)
        result.append(tmp)
        next = tmp
    return result
