#!/usr/bin/python3

def minOperations(n):
    if n <= 0:
        return 0
    operations = 0
    i = 2
    while i <= n:
        operations += 1
        if n % i == 0:
            n = n // i
            i = 2
        else:
            i += 1
    return operations + 1
