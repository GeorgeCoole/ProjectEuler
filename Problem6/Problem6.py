#Project Euler-Problem 6
#Difference of Sum of Squares and Square of Sum
#For first 100 natural numbers

#initialize a list of all of the natural numbers
def initNums(num):
    for i in range(1, num+1):
        nums.append(i)
        
#function to find the sum of all squares
def sumSquares(n):
    squares = []
    squareSum = 0
    for i in range(len(n)):
        sQ = (n[i] * n[i])
        squares.append(sQ)
    for j in range(len(squares)):
        squareSum += squares[j]
    return squareSum

#function to find the square of the sum
def squareSum(r):
    theSum = 0
    for i in range(len(r)):
        theSum += r[i]
    return (theSum * theSum)

#function to find the difference
def difference(x, y):
    return (x-y)


#program main
num = 100                   
nums = []

#initialize numbers
initNums(num)


#sum the squares, store result
res1 = sumSquares(nums)

#square sum, store result
res2 = squareSum(nums)

#get final answer
finalAns = difference(res2, res1)

#see if we did it right
print(finalAns)
