"""You just saw all your answer scripts after correction at school but haven't received a report card yet. So, you want to find out the percentage that you scored. Assume the total marks for each subject to be 80.

Input Format
First line contains the number of subjects n

Next n lines followed by the marks of each subject mi

Output Format
A single line indicating the percentage scored.

The result should be accurate exactly upto 2 decimal places.

Make sure to include the percent symbol."""

# Input the number of subjects
n = int(input())

# Initialize total marks
total_marks = 0

# Input marks for each subject and calculate total marks
for _ in range(n):
    marks = int(input())
    total_marks += marks

# Calculate the percentage
percentage = (total_marks / (80 * n)) * 100

# Print the percentage with two decimal places and the percent symbol
print(f"{percentage:.2f}%")
