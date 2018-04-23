# Project Euler, Problem 1: An Explanation

From Project Euler's website, here is Problem 1.

>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
>
>Find the sum of all the multiples of 3 or 5 below 1000.

Once I read this, I realized that it would be pretty simple to solve this using a Python program. I opened up a new file in IDLE, and quickly got to work. 

The first thing that I'd want to do is write a function that would generate a list of all of the numbers below 1000. I didn't want to have to hard code these in, for obvious reasons. 

Next, I wanted to write a function that would test to see which numbers below 1000 were multiples of three or 5. To do this, I'd just need to implement a simple for loop to iterate through the list of numbers we generated in the first function. A simple check with modulos could help me with this. If the number mod 3 is 0, then it's a multiple of 3. If the number mod 5 is zero, it's a multiple of 5. Then, I would append it to a list specifically created to hold the multiples (god, I love lists in Python. They make my programming life sooooo much easier)

Third, I'd need to go through my list of multiples and add them up.

To review, my rough algorithm was this:
1) Generate a list of 1000 numbers
2) Iterate through the list. If the number can be evenly divided by 3 or 5, it's a multiple of 3 or 5. Add to a separate list of multiples
3) Iterate through the list of multiples, adding them together. Return the sum and print to screen.

It seemed simple. I was suprised at how quickly this came to me. I wrote some code, and ran it. I got an answer, and eagerly, went to the Project Euler website. 

Not a correct answer. 

I went back to the drawing board, trying to see what I needed to do differently. Algorithmically, my program was solid. I just didn't understand what was going wrong.

So, I made a debugging function that could print out an entire list. I ran it, printing out all 1000 of my numbers. It went up to 999. I had a temporary lapse in memory where I forgot that I wasn't supposed to include 1000. So I edited my initNums() function and ran the program again. 

Nope. Still not the right answer. 

Around here, I had an epiphany. *Project Euler had literally given me a test case and I had ignored it.* Stupid me. So, I chaged 1000 to 10, realizing that would help me debug. Once I got the expected answer for 10, I could reasonably assume that I would get the right answer for 1000.

So I tried it with 10. I realized that it was including 10 when the problem description said that it shouldn't. So I fixed that. I wasn't getting the right sum, though. Then I realized that in my multiples function, I was appending the index i instead of the value of i. Whoops. I fixed that, and got the right answer. Then, I tried it with 1000. Nervously, I entered my answer into the Project Euler website. 

Correct!

In the introduction page to this repository, I end my little introduction with a plea:

>If you got here by searching for answers to the Project Euler problems, I only ask that you don't use my solutions to cheat on the problems.

So in the spirit of trying not to help people cheat, I will not be sharing the numerical answer for Problem 1 or any problems. 

However, here's the main takeaways from solving my first Project Euler problem:

1. Printing can be an extremely useful debugging tool, but use it wisely. 
2. Small test cases can be extremely important. 

Going forward, I will remember not to ignore test cases. 

