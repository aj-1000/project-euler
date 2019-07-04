# import required libraries.
from functools import reduce
from itertools import combinations
from operator import mul

# create a list of the largest three digit multiple pairs sorted by product
l = list(combinations([i for i in range(850,999,1)], 2))
l.sort(key=lambda tup: reduce(mul, tup), reverse=True)

# As the product of two large three digit numbers will be six digits. We can test if the first three digits of
# a number, n, match the last three digits reversed.
def palindrome_test(n):
    n = str(n)
    a,b,c = (i for i in n[:3])
    d,e,f = (i for i in n[3:])
    if (a==f) and (b==e) and (c==d):
        return True
    else:
        return False

# loop through products and test if palindrome
for pair in l:
    n = pair[0] * pair[1]
    test = palindrome_test(n)
    if test:
        print('Success! The palindrome is: {}'.format(n))
        break
