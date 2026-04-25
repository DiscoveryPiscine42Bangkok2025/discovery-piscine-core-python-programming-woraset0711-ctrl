#!/usr/bin/env python3

print("Enter a number")

try:
    raw_data = input()
    number = int(raw_data)

    for i in range(10):
        result = i * number

        print(f"{i} x {number} = {result}")

except ValueError:
    print("Error: Please enter a valid integer.")