"""Given a number n, print all the numbers that from 1 to n that are not divisible by 3.

Input Format
The first line indicating the number of test cases - T.

Next T lines will each contain a single number ni.

Output Format
T lines, one for each test case.

Space-seperated and ordered numbers between 1 to ni that are not divisible by 3."""

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the number
    n = int(input())

    # List to store numbers not divisible by 3
    numbers = []

    # Check each number from 1 to n
    for i in range(1, n + 1):
        if i % 3 != 0:  # Check if the number is not divisible by 3
            numbers.append(i)  # Add the number to the list

    # Print the numbers not divisible by 3 for this test case
    print(*numbers)
