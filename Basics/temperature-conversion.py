"""Given a temperature t in Centigrade, convert it into Fahrenheit.

Formula for conversion:

Temp (℉) = (9t / 5) + 32

Input Format
The first line indicating the number of test cases T

Next T lines contains the temperature in Centigrade - ti (can be decimal values).

Output Format
T lines each indicating the temperature in fahrenheit.

The fahrenheit values are accurate to upto exactly 2 decimal places."""

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input the temperature in Celsius
    temp_celsius = float(input())

    # Convert Celsius to Fahrenheit
    temp_fahrenheit = (9 * temp_celsius / 5) + 32

    # Print the temperature in Fahrenheit rounded to 2 decimal places
    print("{:.2f}".format(temp_fahrenheit))