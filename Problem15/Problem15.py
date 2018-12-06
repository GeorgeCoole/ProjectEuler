#Project Euler Problem 15
#Lattice Paths
#How Many Lattice Paths in a 20 x 20 Grid?

#import modules
import scipy.special

#program main
def main():
    #m+n C n is the number of lattice paths in an m x n grid
    print(scipy.special.comb(40, 20, exact=True))
    
#execute main
main()
