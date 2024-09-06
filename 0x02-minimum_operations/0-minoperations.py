#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.

-Prototype: def minOperations(n)
-Returns an integer
-If n is impossible to achieve, return 0
Example:
n = 9
H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH =>
Paste => HHHHHHHHH
Number of operations: 6
"""


def minOperations(n):
    """calculate fewer number of operations"""
    # Determine the prime factorization of n
    factors = []

    # Divide with 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # if n is still greater than 2, then n itself is a prime factor
    if n > 2:
        factors.append(n)

    # Sum all values in factors to obtain the minimum operation
    min_oper = 0
    for num in factors:
        min_oper += num

    return min_oper
