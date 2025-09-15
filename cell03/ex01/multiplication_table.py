#!/usr/bin/env python3
num = int(input("Enter a number: ").strip())
i = 0
while i < 10:
    mult = num * i
    print(f"{num} x {i} = {mult}")
    i += 1