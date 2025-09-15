#!/usr/bin/env python3
num = int(input("Enter a number: ").strip())

if num > 25:
    print("ERROR\n")
else:
    while num < 26:
        print(f"Inside the loop, my variable is {num}")
        num += 1