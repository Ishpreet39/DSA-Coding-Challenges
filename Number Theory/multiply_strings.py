"""Given two numbers as strings s1 and s2. Calculate their Product.

Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:

Input:
s1 = "0033"
s2 = "2"
Output:
66
Example 2:

Input:
s1 = "11"
s2 = "23"
Output:
253"""

class Solution:
    def multiplyStrings(self,s1,s2):
        # code here
        # return the product string
        a=0
        for i in s1:
            if i==0:
                continue
            elif i=='-':
                continue
            else:
                a=a*10+int(i)
        if s1[0]=='-':
            a=-a
        b=0
        for i in s2:
            if i==0:
                continue
            elif i=='-':
                continue
            else:
                b=b*10+int(i)
        if s2[0]=='-':
            b=-b
        return a*b