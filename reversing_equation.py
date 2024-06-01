"""Given a mathematical equation that contains only numbers and +, -, *, /. Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
It is guaranteed that the given equation is valid, and there are no leading zeros.

Example 1:

Input:
S = "20-3+5*2"
Output: 2*5+3-20
Explanation: The equation is reversed with
numbers remaining the same.
Example 2:

Input: 
S = "5+2*56-2/4"
Output: 4/2-56*2+5
Explanation: The equation is reversed with
numbers remaining the same."""

class Solution:
    def reverseEqn(self, s):
        # code here
        def split_equation(s):
            equation = []
            num = ""
            for char in s:
                if char.isdigit():
                    num += char
                else:
                    if num:
                        equation.append(num)
                        num = ""
                    equation.append(char)
            if num:
                equation.append(num)
            return equation
        
        # Reverse the numbers and join them with operators
        equation_parts = split_equation(s)
        reversed_equation = "".join(equation_parts[::-1])
        return reversed_equation