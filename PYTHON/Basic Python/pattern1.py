"""
Number Pattern Generator

This script generates a right-angled triangular number pattern based on user input.

Author: Adwaith Jayan
Date: 2025-02-23

Usage:
------
Run the script and input a positive integer `n`. The script will print a number pattern up to `n` rows.

Description:
------------
- The script prompts the user to enter a positive integer `n`.
- It uses nested loops to generate and print the number pattern.
- The outer loop controls the number of rows.
- The inner loop prints numbers from 1 to the current row number.

Example:
--------
Input:
    n: 5

Output:
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

Notes:
------
- The script assumes the user enters a valid positive integer.
- Formatting ensures numbers in each row are printed with a space separator.

"""

n = int(input("n:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print("")

