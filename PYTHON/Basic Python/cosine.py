"""
Cosine Series Approximation

This script calculates the cosine of a given angle using the Maclaurin series expansion.

Author: Adwaith Jayan
Date: 2025-02-23

Usage:
------
Run the script and input the number of terms for the series expansion and the angle in degrees.
The script will compute the cosine value using the series approximation.

Description:
------------
- The script prompts the user to enter the number of terms (`n`) for the approximation.
- It then asks for the angle `x` in degrees and converts it to radians.
- Using a loop, the script computes the sum of the series up to `n` terms.
- Finally, it prints the computed cosine value.

Example:
--------
Input:
    No of terms? 5
    Enter x in degrees 45

Process:
    cos(45) ≈ 1 - (45^2)/2! + (45^4)/4! - (45^6)/6! + (45^8)/8!

Output:
    Sum= 0.7071067811865475

Notes:
------
- The accuracy improves as `n` increases.
- The script assumes valid numerical inputs.
- For very large `n`, floating-point precision may affect the results.

"""

import math

n = int(input("No of terms? "))
x = math.radians(float(input("Enter x in degrees")))
cos_x = 0
for i in range(n):
    cos_x += (((-1)**i) * (x**(2*i))) / (math.factorial(2*i))
print("Sum=", cos_x)

