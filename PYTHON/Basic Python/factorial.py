"""
Factorial Calculator

This script calculates the factorial of a given number using a while loop.

Author: [Adwaith Jayan]
Date: [23-02-2025]

Usage:
------
Run the script and input a positive integer when prompted. The script will then compute and display the factorial of the entered number.

Description:
------------
- The script prompts the user to enter a number.
- It initializes the factorial variable `fact` to 1.
- It uses a while loop to multiply `fact` by the current value of `num`, decrementing `num` until it reaches zero.
- Finally, it prints the calculated factorial.

Example:
--------
Input:
    Enter number: 5

Process:
    5! = 5 × 4 × 3 × 2 × 1 = 120

Output:
    Factorial = 120

Notes:
------
- The script assumes the input is a positive integer.
- If the user enters 0, the output will be 1 (as 0! = 1).
- Negative inputs are not handled explicitly.

"""

num = int(input("Enter number: "))

fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial =", fact)

