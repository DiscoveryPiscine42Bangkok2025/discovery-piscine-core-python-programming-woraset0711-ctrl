#!/usr/bin/env python3
import sys

def main(): 
    if len(sys.argv) == 2:
        result = sys.argv[1].upper()
        print(result)
    else:
        print("none")

if __name__ == "__main__":
    main()