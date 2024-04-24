"""You had your birthday party last night and received a lot of candies. You do not want keep so many and decide to distribute it among your friends. To make things interesting, you plan to give each friend a number of candies equal to the number of vowels in thier first name.

You can assume that the first name of your friends consists of only one word (no spaces or special characters) and you have enough candies for each of them.

You have to determine how many candies each of your friend gets.

Input Format
First line has a number n representing the number of your friends.

n lines follow with the first name of each of your friends all in separate lines.

Output Format
n lines, each indicating the number of candies the person received."""

def count_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

# Input the number of friends
n = int(input())

# Process each friend
for _ in range(n):
    # Input the friend's first name
    first_name = input()

    # Count the number of vowels in the first name
    candies = count_vowels(first_name)

    # Print the number of candies the friend received
    print(candies)