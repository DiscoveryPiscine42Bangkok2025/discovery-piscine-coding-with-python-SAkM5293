#!/usr/bin/env python3
num1 = input("Enter the first number: ").strip()
num2 = input("Enter the second number: ").strip()

mult = int(num1) * int(num2)
print(f"{num1} x {num2} = {mult}")

if mult < 0:
    print("The result is negative.")
elif mult > 0:
    print("The result is positive.")
else:
    print("The result is zero.")