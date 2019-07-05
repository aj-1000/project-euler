# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.  
# Find the sum of all the primes below two million.  

# import required libraries
import numpy as np
from itertools import compress

# build sieve of eratosthenes
def generate_primes_to(n):
    '''
    A function that generates primes to n using the sieve of eratosthenes algorithm
    '''
    # initialise array of True length, n, and set 0 and 1 to False (as 0 and 1 are not prime)
    boolean_primes = np.ones(n, dtype=bool)
    boolean_primes[0], boolean_primes[1] = (False,False)

    # loop through integers up until n, turning off multiples of each prime number
    for i in range(2,n):

        # check if prime
        if boolean_primes[i]:
            
            # create list of multiples and switch off
            non_p = [j for j in range(i**2, n, i)]
            for x in non_p:
                boolean_primes[x] = False
        
    return list(compress(list(range(n)), boolean_primes))  

print(sum(generate_primes_to(2000000)))
