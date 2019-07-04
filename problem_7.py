# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# import required libraries
from itertools import count

# Using the prime test from a previous problem
def test_if_prime(x):
    if x == 2:
        return True 
    elif x%2 == 0: # check that x is not even
        return False
    else:
        # loop through the odd integers between 3 and x/2
        for i in [j for j in  range(3,(x//2)+1,2)]:
            if x%i == 0:
                return False
    return True

# set initial variables
candidate = 2
primes = []
target = 10001
arr = count(3,2)

# loop through primes
while len(primes) != target:
    found_prime = test_if_prime(candidate)
    if found_prime:
        primes.append(candidate)
    candidate = next(arr) 

# print result
print(primes[-1])
