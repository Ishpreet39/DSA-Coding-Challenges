"""Given a number n.Find if the digit sum(or sum of digits) of n is a Palindrome number or not.

Note: A Palindrome number is a number that stays the same when reversed. Example- 121 , 131 , 7 etc.

Example 1:

Input:
n = 56
Output: 1
Explanation:
The digit sum of 56 is 5+6=11.Since, 11 is a palindrome number.Thus, answer is 1.
Example 2:

Input:
n = 98
Output: 0
Explanation:
The digit sum of 98 is 9+8=17. Since 17 is not a palindrome,thus, answer is 0."""

class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        def calculateDigitSum(num):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum
        
        # Function to check if a number is a palindrome
        def isPalindrome(number):
            return str(number) == str(number)[::-1]
        
        digit_sum = calculateDigitSum(n)
        return int(isPalindrome(digit_sum))

