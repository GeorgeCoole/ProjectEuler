#Project Euler
#Palindrome Numbers
#Find the largest palindrome made from 3 digit numbers

#function to check for palindrome
def isPalindrome(n):
    pal = str(n)
    if (pal == pal[::-1]):
        return True
    else:
        return False

#function to generate potential palindromes
# b denotes the lower bound or bottom
# t denotes the upper bound or top
def findLargestPal(b, t):
    biggest = 0
    for i in range(t, b, -1):
        for j in range(t, b, -1):
            if isPalindrome(i * j):
                if i * j > biggest:
                    biggest = i*j
    return biggest


#program main

upper = 999
lower = 100

answer = findLargestPal(lower, upper)

print(answer)

