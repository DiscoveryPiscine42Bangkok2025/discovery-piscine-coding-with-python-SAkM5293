#!/usr/bin/env python3
num = int(input("Please tell me your age:").strip())
print(f"You are currently {num} years old.")
for i in range(1, 4):
    print(f"In {i*10} year(s) you will be {num + (i*10)} years old.")