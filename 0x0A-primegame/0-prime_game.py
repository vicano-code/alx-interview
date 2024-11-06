#!/usr/bin/python3
"""
Determine winner in a a game of prime selection
"""


def isprime(n):
    """check if a number is prime"""
    # check if n is less than 2
    if n <= 1:
        return False
    # check for divisors from 2 to sqrt of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determine the winner in a game of prime selection"""
    # determine the winner in a game
    wins = {
        'Maria': 0,
        'Ben': 0
    }
    for n in nums:
        if n == 1:  # No prime so Maria does not pick
            wins['Ben'] += 1

        x = [i for i in range(1, n+1)]
        # print(x)
        # check if prime number in x
        _isprime = False
        for i in x:
            if isprime(i):
                _isprime = True
                break

        if _isprime:
            turns = []
            next_turn = 'Maria'
            while any(isprime(i) for i in x):
                for i in x:
                    if isprime(i):
                        turns.append(next_turn)
                        next_turn = 'Ben' if next_turn == 'Maria' else 'Maria'

                # Remove i and its multiples from x
                x = [k for k in x if k % i != 0]
                break

            wins[turns[-1]] += 1

    if wins['Maria'] > wins['Ben']:
        winner = 'Maria'
    elif wins['Maria'] < wins['Ben']:
        winner = 'Ben'
    else:
        winner = None

    return winner
