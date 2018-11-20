# This problem was asked by Square.

# The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
# The method is to take increasingly larger prime numbers, and mark their multiples as composite.

# For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] 
# (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. 
# Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.

# Implement this algorithm.

# Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

def findAllPrime(n):
    l = [True] * 101
    l[0] = False
    l[1] = False
    for i in range(2, n):
        j = i * 2
        while j <= 100:
            print(j)
            l[j] = False
            j = j + i
    output = []
    for index, val in enumerate(l):
        if val == True:
            output.append(index)
    print(output)

findAllPrime(50)
# n doesn't even seem to matter