"""Given the temperature and humidity for the day, determine which category the day's weather falls into.

Temperature (°C)	Humidity (%)	Weather
>=30	            >=90	        Hot and Humid
>=30	            <90	            Hot
<30	                >=90	        Cool and Humid
<30	                <90	            Cool
Input Format
The first line has an integer indicating the number of test cases T

Next T lines should contain two space-separated integers denoting the temperature and humidity

Output Format
T lines each indicating the weather based on the table shown above."""

# Input the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Input temperature and humidity
    temperature, humidity = map(int, input().split())

    # Determine the weather category
    if temperature >= 30 and humidity >= 90:
        print("Hot and Humid")
    elif temperature >= 30 and humidity < 90:
        print("Hot")
    elif temperature < 30 and humidity >= 90:
        print("Cool and Humid")
    else:
        print("Cool")