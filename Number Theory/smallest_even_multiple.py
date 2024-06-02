"""Given a positive integer n, return the smallest positive integer that is a multiple of both 2 and n.
 

Example 1:

Input: n = 5
Output: 10
Explanation: The smallest multiple of both 5 and 2 is 10.
Example 2:

Input: n = 6
Output: 6
Explanation: The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself."""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def lcm(a, b):
            # Calculate the least common multiple (LCM) of two numbers
            gcd = self.gcd(a, b)
            return (a * b) // gcd

        def gcd(a, b):
            # Calculate the greatest common divisor (GCD) of two numbers using Euclid's algorithm
            while b:
                a, b = b, a % b
            return a

        # The smallest multiple of both 2 and n is their least common multiple (LCM)
        n1 = n[0]  # Assuming the input list contains only one positive integer
        return lcm(2, n1)