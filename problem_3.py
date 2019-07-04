# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math
n = 600851475143

def test_if_prime(x):
    if x%2 == 0: # check that x is not even
        return False
    else:
        # loop through the odd integers between 3 and x/2 
        for i in [j for j in  range(3,(x//2)+1) if j%2 != 0]:
            if x%i == 0:
                return False
    return True
                 
def largest_prime_factor(n):
    limit = int(math.sqrt(n)) + 1
    arr = []
    for i in range(2,limit):
        if n%i == 0:
            prime = test_if_prime(i)
            if prime:
                arr.append(i)
    return arr[-1]

print(largest_prime_factor(n))
