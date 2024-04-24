"""Given an integer matrix (2D array) of dimension m*n (m rows, n columns), find out the largest integer in the entire matrix."""
# Input the number of rows and columns
m, n = map(int, input().split())

# Initialize the maximum value as negative infinity
max_value = float('-inf')

# Input the matrix elements and find the maximum value
for _ in range(m):
    row = list(map(int, input().split()))
    max_value = max(max_value, max(row))

# Print the maximum value in the matrix
print(max_value)
