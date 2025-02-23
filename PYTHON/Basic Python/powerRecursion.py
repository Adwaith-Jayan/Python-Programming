"""
Recursive Power Function

This script defines a recursive function to compute the power of a number.

Author: Adwaith Jayan
Date: 2025-02-23

Usage:
------
Call the `power(x, y)` function with a base `x` and an exponent `y` to obtain the result of `x^y`.

Description:
------------
- The function `power(x, y)` computes `x` raised to the power `y` recursively.
- If `y` is 0, it returns 1 (base case: x^0 = 1).
- If `y` is 1, it returns `x` (base case: x^1 = x).
- Otherwise, it recursively calculates `x * power(x, y-1)`.

Example:
--------
Input:
    power(2, 3)

Process:
    power(2, 3) = 2 * power(2, 2)
    power(2, 2) = 2 * power(2, 1)
    power(2, 1) = 2

Output:
    8

Notes:
------
- This implementation uses recursion and may not be optimal for large values of `y`.
- Consider using an iterative or divide-and-conquer approach for better efficiency.

"""

def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    return x * power(x, y - 1)

