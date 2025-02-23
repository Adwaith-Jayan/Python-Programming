"""
Fibonacci Sequence Generator

This script defines a recursive function to compute the Fibonacci sequence.

Author: Adwaith Jayan
Date: 2025-02-23

Usage:
------
Call the `fib(k)` function with a positive integer `k` to obtain the k-th Fibonacci number.

Description:
------------
- The function `fib(k)` calculates the Fibonacci sequence recursively.
- If `k` is 1, it returns 0 (the first Fibonacci number).
- If `k` is 2, it returns 1 (the second Fibonacci number).
- For larger values of `k`, it recursively computes `fib(k-1) + fib(k-2)`.

Example:
--------
Input:
    fib(5)

Process:
    fib(5) = fib(4) + fib(3)
    fib(4) = fib(3) + fib(2)
    fib(3) = fib(2) + fib(1)
    fib(2) = 1, fib(1) = 0

Output:
    3

Notes:
------
- This implementation uses recursion and may be inefficient for large values of `k`.
- Consider using memoization or an iterative approach for better performance.

"""

def fib(k):
    if k == 1:
        return 0
    elif k == 2:
        return 1
    return fib(k-1) + fib(k-2)

