#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) == 2:
        input_string = sys.argv[1]

        z_found = [char for char in input_string if char == 'z']

        if z_found:
            print("".join(z_found))
        else:
            print("none")
    else:
        print("none")

if __name__ == "__main__":
    main()