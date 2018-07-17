#Project Euler Problem 16
#Power Digit Sum
#What is the sum of the digits of 2^1000

#function to sum the digits of the number when we get it
def digitSum(n):
    theSum = 0
    for d in n:
        theSum += int(d)
    return theSum

#program main

testNum = 2**1000
num = str(testNum)
print(digitSum(num))

