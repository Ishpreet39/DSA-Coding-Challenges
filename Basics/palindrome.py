"""A palindrome is a word that reads the same backward as forward, e.g., madam. If you start comparing the letters from the beginning with the corresponding letters from the end, they would be the same.

Given a set of words, you have to find if they are palindrome or not.

Input Format
First line contains an integer T denoting the number of words to check.

Next T lines contain a word each without any special characters.

Output Format
T lines, each denoting if the corresponding word is a palindrome.

"True" if the word is a palindrome and "False" if it is not."""

# Input the number of words to check
T = int(input())

# Process each word
for _ in range(T):
    # Input the word
    word = input()

    # Check if the word is a palindrome
    is_palindrome = word == word[::-1]

    # Print True or False based on the palindrome check
    print(is_palindrome)