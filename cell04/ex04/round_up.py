#!/usr/bin/env python3

num_str = input("Give me a number: ")

num = float(num_str)
if int(num) == 0:
    rounded = 0
elif int(num) == num:
    rounded = int(num) 
else:
    rounded = int(num) + 1
print(rounded)