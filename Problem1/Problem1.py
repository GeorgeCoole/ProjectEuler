#Project Euler-Problem 1
#Multiples of 3 and 5
#Find the sum of all the multiples of 3 or 5 below 1000


#function to initialize a list of 1000 integers
def initNums():
    for i in range(1,1000): 
        nums.append(i)

#function to sort through multiples
def processMultiples(nums):
    for i in range(len(nums)):
        if (nums[i] % 3 == 0 or nums[i] % 5 == 0):
            multiples.append(nums[i])

#function to get the sum
def addMultiples(multiples):
    theSum = 0
    for i in range(len(multiples)):
        theSum += multiples[i]

    return theSum


#program main

#list for numbers
nums = []
#list for multiples
multiples = []

#call function to initialize numbers
initNums()

#call function to process multiples
processMultiples(nums)

#call function to add numbers, get answer
ans = addMultiples(multiples)

print(ans)

