/***************************************************** 
Project Euler Problem 12
Triangle Numbers
Find the first triangle number with over 500 divisors
*******************************************************/

//import modules
#include <iostream>
#include <cmath>

using namespace std;

//function prototypes
int triangle(int n);
int numDivisors (int k);

/*******************
Program Main
********************/
int main()
{
	int targetNum = 500;
	int test = 1;
	int finalAnswerAlex = 0;

	while(finalAnswerAlex < targetNum)
	{
		test++;
		finalAnswerAlex = numDivisors(triangle(test));
	}
	cout << "The answer is " << triangle(test) << endl;
	return 0;
}

/****************************************************************
Function: triangle
returns the nth triangle number using the formula n * (n+1) / 2
*****************************************************************/
int triangle(int n) 
{
	int n1 = n + 1;
	int ans = (n * n1)/2;
  	return (ans);
}

/****************************************************************
Function: numDivisors
Returns the number of divisors of a given number
*****************************************************************/
int numDivisors (int k)
{
	int root=0, count=0;
	root = floor(sqrt(k));
	for(int i = 1; i <= root; i++)
	{
		if(k % i == 0 && i * i != k)
		{
			count+=2;
		}
		if (i * i == k)
		{
			count--;
		}
	}
	
	return count;
}
