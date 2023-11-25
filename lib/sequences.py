#!/usr/bin/env python3

def print_fibonacci(length):
 
 if length <= 0:
    print([])
 else: 
    fib_sequence = [0, 1]
    if length == 1:
        print ([0])
    elif length == 2:
       print(fib_sequence)
    else:
       for _ in range(2, length):
          next_number = fib_sequence[-1] + fib_sequence [-2]
          fib_sequence.append(next_number)
          print(fib_sequence)