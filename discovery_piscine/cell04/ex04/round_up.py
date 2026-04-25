#!/usr/bin/env python3
import math

def main():
    user_input = input("Give me a number: ")

    try:
        number = float(user_input)

        result = math.ceil(number)

        print(result)
            
    except ValueError:
        pass

if __name__ == "__main__":
    main()