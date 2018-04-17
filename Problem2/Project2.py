#Project Euler-Problem 2
#Even Fibonacci Numbers
#For values less than 4 mil, find the sum of even terms

#function for finding fibonacci numbers
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

def initFib():
    for i in range(0, 40):
        newFib = fib(i)
        fibs.append(newFib)
    
#function to get even fib numbers
def getEvenFibs(fibs):
    for i in range(len(fibs)):
        if (fibs[i] % 2 == 0) and (fibs[i] < MAXFIBVAL):
            evenFibs.append(fibs[i])
            
#function to get sum
def sumEvenFibs(evenFibs):
    fibSum = 0
    for i in range(len(evenFibs)):
        fibSum += evenFibs[i]
    return fibSum

#program main
#max fib value
MAXFIBVAL = 4000000
#list to store fibonacci numbers
fibs = []

#list to store evens
evenFibs = []

#whoops forgot a function call
initFib()
#find the even fibonacci numbers
getEvenFibs(fibs)

#get the sum
answer = sumEvenFibs(evenFibs)

#print the sum
print(answer)


