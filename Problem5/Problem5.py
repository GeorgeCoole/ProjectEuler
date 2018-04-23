#Project Euler-Problem 5
#Smallest Multiple
#2520 is the smallest number evenly divisble by 1-10.
#Find the smallest number evenly divisible by 1-20

#import fractions module for the gcd function
import fractions

#function to calculate lcm using euclid's algorithm

def eucLcm(n):
    ourNum = 1
    for i in range(1, n+1):
        ourNum = (ourNum * i) / (fractions.gcd(ourNum, i))
    return ourNum

#program main

num = 20

print(int(eucLcm(num)))
