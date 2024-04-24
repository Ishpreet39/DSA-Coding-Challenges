"""Given a number, find out if it is odd or even.

There are multiple tests in this.

Input Format
First line indicating the number of test cases T.

Next T lines containing a number each ni where i denotes the ith input.

Output Format
T lines each indicating the answer for the ith input.

Each line says "ODD" if the number is odd and "EVEN" if the number is even."""

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the number for the test case
    num = int(input())

    # Check if the number is odd or even
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
