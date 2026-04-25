#!/usr/bin/env python3

def main():
    try:
        age_str = input("Please tell me your age: ")
        
        current_age = int(age_str)
        print(f"You are currently {current_age} years old.")
        print(f"In 10 years, you'll be {current_age + 10} years old.")
        print(f"In 20 years, you'll be {current_age + 20} years old.")
        print(f"In 30 years, you'll be {current_age + 30} years old.")
        
    except ValueError:
        print("Please enter a valid number for age.")

if __name__ == "__main__":
    main()