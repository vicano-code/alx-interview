#!/usr/bin/python3
"""
Determine winner in a a game of prime selection
"""


def isprime_sieve(n):
    """
    Use sieve of Eratosthenes to mark prime numbers up to n
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """
    Determine the winner of prime selection game
    """
    # input validation
    if x < 1 or len(nums) != x:
        return None
    # Precompute primes up to the maximum possible n in nums
    max_n = max(nums) if nums else 0
    sieve = isprime_sieve(max_n)

    # Track wins for each player
    wins = {'Maria': 0, 'Ben': 0}

    # Determine the winner for each round
    for n in nums:
        moves = 0
        available_nums = list(range(1, n + 1))
        for i in range(2, n + 1):
            if sieve[i] and i in available_nums:
                # If i is a prime, make a move and remove i and its multiples
                moves += 1
                available_nums = [x for x in available_nums if x % i != 0]

        # Determine the winner based on the number of moves
        if moves % 2 == 1:
            # Maria wins (since she starts first)
            wins['Maria'] += 1
        else:
            # Ben wins
            wins['Ben'] += 1

    # Determine the overall winner
    if wins['Maria'] > wins['Ben']:
        return 'Maria'
    elif wins['Maria'] < wins['Ben']:
        return 'Ben'
    else:
        return None
