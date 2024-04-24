"""A binary number is a number composed of 0s and 1s.
Given a binary number, check if the number has adjacent zeroes or not, i.e., if two zeroes are present side by side or not.

Input Format
The first line contains T - no. of test cases.

Next T lines each containing one binary number N.

Output Format
"Yes" if the number has adjacent zeroes
"No" if the number does not have adjacent zeroes"""

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the binary number as a string
    binary_number = input()

    # Check if the binary number has adjacent zeroes
    has_adjacent_zeroes = False
    for i in range(len(binary_number) - 1):
        if binary_number[i] == '0' and binary_number[i + 1] == '0':
            has_adjacent_zeroes = True
            break

    # Print the result for this test case
    if has_adjacent_zeroes:
        print("Yes")
    else:
        print("No")