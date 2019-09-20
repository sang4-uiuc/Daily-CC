# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
# For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

def cons(a, b):
    return lambda f : f(a, b)
# Implement car and cdr.

def car(f):
    def left(a, b):
        return a
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)

# def cdr(p):
#     return 

# car = cons(3,4)
print(car(cons(3, 4)))
# print(car(min))