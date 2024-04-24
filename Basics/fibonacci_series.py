"""Given a number (n), print the first n fibonacci numbers.

Example:
The first 6 fibonacci numbers are 0 1 1 2 3 5.

Input Format
The first line contains T denoting the no. of test cases.
Next T lines each containing a number.

Output Format
The first n fibonacci numbers."""

# Function to generate the first n Fibonacci numbers
def generate_fibonacci(n):
    fibonacci_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers
    for i in range(2, n):
        fibonacci_numbers.append(fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1])  # Calculate the next Fibonacci number
    return fibonacci_numbers[:n]  # Return the first n Fibonacci numbers

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the number n
    n = int(input())
    # Generate the first n Fibonacci numbers
    fibonacci_sequence = generate_fibonacci(n)
    # Print the first n Fibonacci numbers separated by spaces
    print(*fibonacci_sequence)
