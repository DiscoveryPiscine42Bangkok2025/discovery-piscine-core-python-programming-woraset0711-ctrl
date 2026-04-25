#!/usr/bin/env python3

def add_one(nb):
    nb += 1

def main():
    my_var = 42
    print(f"Before: {my_var}")
    add_one(my_var)
    print(f"After: {my_var}")

if __name__ == "__main__":
    main()