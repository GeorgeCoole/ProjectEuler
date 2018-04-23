#Project Euler-Problem 3
#Largest Prime Factor
#Find the largest prime factor of 600851475143

#import math for functions
import math as m

#function to find square root and floor until we have a factor
def floorIt(n):
    upBound = m.sqrt(n)
    floor = m.floor(upBound)
    if (n%floor==0) and isPrime(floor):
        return floor
    else:
        while True:
            for i in range(floor, 1, -1):
                if (n%i==0) and isPrime(i):
                    break
            return i

#function to test primality of floor
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

#program main

num = 600851475143

#call to floor the square root of our number
ans = floorIt(num)

print(ans)
