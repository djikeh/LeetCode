#!/usr/bin/env python3

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Note: Given n will be a positive integer.
"""

from random import randint

def number_of_ways(steps):
    """
    Return the number of ways to climb to the top.
    """
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    pre, cur = 1, 2
    tmp = 0
    for _ in range(2, steps+1):
        tmp = cur
        cur += pre
        pre = tmp
    return cur

def main():
    """
    Main programm
    """
    print(list(map(number_of_ways, [randint(1, 100) for _ in range(5)])))

main()
