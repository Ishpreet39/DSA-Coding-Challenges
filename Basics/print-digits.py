"""Given a two-digit number n, print both the digits of the number.

Input Format
The first line indicating the number of test cases T.

Next T lines will each contain a single number ni.

Output Format
T lines each containing two digits of the number ni separated by space."""

T = int(input())

# Process each test case
for _ in range(T):
    # Input the two-digit number
    num = int(input())

    # Convert the number to a string
    num_str = str(num)

    # Print the two digits separated by space
    print(num_str[0], num_str[1])
