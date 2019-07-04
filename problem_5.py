# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def greatest_common_denominator(a,b):
    """
    An implementation of the Euclidean algorithm
    """
    while b!=0:
        dummy = b
        b = a % b
        a = dummy
    return a

def lowest_common_multiple(arr):
    a,b = (i for i in arr[:2])
    lcm_1 =  int((a*b) / greatest_common_denominator(a,b))
    if len(arr) == 2:
        return lcm_1     
    if len(arr) > 2:
        return lowest_common_multiple([lcm_1]+arr[2:])

print(lowest_common_multiple(list(range(1,21))))
