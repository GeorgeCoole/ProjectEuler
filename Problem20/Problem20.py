#Project Euler Problem 20
#Factorial Digit Sum
#Find the sum of the digits in 100!

#import modules
import math

#digitSum-adds the digit up
def digitSum(n):
    theSum = 0
    for d in n:
        theSum += int(d)
    return theSum

#program main
def main():
    num = str(math.factorial(100))
    print(digitSum(num))

#execute main
main()
