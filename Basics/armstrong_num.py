"""A number is known as an Armstrong number if the sum of the cubes of all its digits is equal to the number itself.

Input Format
The first line contains T denoting the no. of test cases.
Next T lines each containing a number.

Output Format
T lines each containing "Yes" (if number is an Armstrong Number) or "No" (if the number is not an armstrong number)."""

# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    # Convert the number to a string to iterate through its digits
    num_str = str(num)
    # Calculate the sum of cubes of digits
    digit_sum_cubes = sum(int(digit) ** 3 for digit in num_str)
    # Check if the sum of cubes is equal to the number
    return digit_sum_cubes == num

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the number
    num = int(input())
    # Check if the number is an Armstrong number and print the result
    if is_armstrong_number(num):
        print("Yes")
    else:
        print("No")
