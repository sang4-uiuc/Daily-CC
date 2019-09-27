
# This problem was asked by Apple.

# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
from time import sleep

def job(f, n):
    sleep(n/1000)
    f()

def test():
    print("Printing")

job(test, 5000)
