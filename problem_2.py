def fib_gen(limit, sequence=[1,1]):
    sequence.append(sequence[-1] + sequence[-2])
    if sequence[-1] > limit:
        sequence.pop()
        return sequence
    else:
        return fib_gen(limit, sequence)

def even_sum(arr):
    even_arr = [i for i in arr if i%2==0]
    return sum(even_arr)

def euler_solver(n):
    return even_sum(fib_gen(n))

print(euler_solver(4000000))