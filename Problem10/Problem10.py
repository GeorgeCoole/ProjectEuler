#Project Euler
#Problem 10
#Find the sum of all the primes below 2 million

#function to generate a list of primes to certain number
def genPrimes(n):
    for i in range(1, n):
        if isPrime(i):
            primes.append(i)

#function to test primality of numbers
def isPrime(f):
    if f <= 1:
        return False
    elif f <= 3:
        return True
    elif f % 2 == 0 or f%3 == 0:
        return False
    i = 5
    while i*i <= f:
        if f % i == 0 or f % (i+2) == 0:
            return False
        i = i + 6
    return True

#function to get sum of primes
def getSum(p):
    theSum = 0
    for i in range(len(p)):
        theSum += p[i]
    return theSum

#program main

#list to hold primes
primes = []

#number we're summing primes for
num = 2000000 #10 is test case, 2 million is our main case

#get our prime numbers
genPrimes(num)

#find the sum
answer = getSum(primes)

#print answer to the screen
print(answer)

