# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# import required functions
from operator import mul, add
from functools import reduce

# define helper functions
def primitive_triple_calculator(m,n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return (a,b,c)

def non_primitive_triple_generator(a,b,c,limit):
    # generate non-primitive (np) triples by multiplying by k until c > limit
    triples = set()
    k,np_c = 2,0
    while np_c < limit:
        np_a, np_b, np_c = (k*a, k*b, k*c)
        triples.add((np_a,np_b,np_c))
        k += 1
    return triples 

# define function to generate pythagorean triples using Euclid's formula
def pythagorean_triple_generator(limit):
    '''
    A function that generates all pythagorean triples where c is less than a limit
    '''
    # initialize variables
    c, m = 0, 2
    triples = set()

    # while c is less than the limit
    while c < limit:

        # loop through all values of n up to m
        for n in range(1,m):

            # generate primitive triple and add to set of triples
            a,b,c = primitive_triple_calculator(m,n)
            triples.add((a,b,c))
            
            # update triples set with non-primitive triples
            triples.update(non_primitive_triple_generator(a,b,c,limit))
                   
        # increase m by 2 (as m and n cannot both be odd there is no need to increment by 1)
        m += 2

    return triples

# loop through triples and search for success
for tup in pythagorean_triple_generator(500):
    if reduce(add, tup) == 1000:
        print(reduce(mul, tup)) 
