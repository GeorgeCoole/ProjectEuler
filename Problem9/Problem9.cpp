//Project Euler Problem 9
//Special Pythagorean Triplet
//Find abc for the Pythagorean Triplet where a+b+c = 1000

#include <iostream>
#include <cmath>

using namespace std;

//function prototypes
bool isTriple(int a, int b, int c);
int getResult (int d);

//program main
int main()
{
    
    int answer = getResult(1000);
    
    cout << answer << endl;
    
    return 0;
}

//isTriple-returns whether or not a, b, and c make a pythagorean triple
bool isTriple(int a, int b, int c)
{
    return (c * c==((a*a)+(b*b)));
}

//function to process results
int getResult(int d)
{
    for (int a = 1; a <= 500; a++)
    {
        for (int b = 1; b <= 500; b++)
        {
            int c = d - b - a;
            if (isTriple(a, b, c) && a < b)
            {
                return a * b * c;
            }
        }
    }
    return 0;
}
