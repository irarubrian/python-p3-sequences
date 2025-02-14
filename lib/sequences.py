#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])  # Edge case: if length is 0 or negative, return an empty list
        return
    
    fibonacci = [0, 1]  # Start with the first two numbers
    for _ in range(2, length):  # Generate remaining numbers
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
    print(fibonacci[:length])  # Print only up to the given length


