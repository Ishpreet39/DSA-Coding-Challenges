"""Given a number, find the sum of its digits.

If the number is represented as d1d2d3d4d5, then the sum will be d1 + d2 + d3 + d4 + d5.

Input Format
The first line contains T denoting the no. of test cases
Next T lines each containing a number

Output Format
For each test, a line with sum of digits of the number"""

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the number as a string
    num_str = input()

    # Calculate the sum of digits
    digit_sum = sum(int(digit) for digit in num_str)

    # Print the sum of digits for this test case
    print(digit_sum)
