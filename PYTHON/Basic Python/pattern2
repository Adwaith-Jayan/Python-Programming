"""
Alphabet Pattern Generator

This script generates a right-angled triangular alphabet pattern based on user input.

Author: Adwaith Jayan
Date: 2025-02-23

Usage:
------
Run the script and input a positive integer `n`. The script will print an alphabet pattern up to `n` rows.

Description:
------------
- The script prompts the user to enter a positive integer `n`.
- It uses nested loops to generate and print the alphabet pattern.
- The outer loop controls the number of rows.
- The inner loop prints letters from 'A' to the corresponding letter in the row.

Example:
--------
Input:
    n: 5

Output:
    A
    A B
    A B C
    A B C D
    A B C D E

Notes:
------
- The script assumes the user enters a valid positive integer.
- Formatting ensures letters in each row are printed with a space separator.

"""

n = int(input("n:"))
for i in range(1, n + 1):
    for j in range(ord('A'), ord('A') + i):
        print(chr(j), end=" ")
    print("")

