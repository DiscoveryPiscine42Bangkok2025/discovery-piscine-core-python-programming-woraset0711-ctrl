#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) >= 3:

        params = sys.argv[1:]

        params.reverse()

        for item in params:
            print(item)
    else:
        print("none")

if __name__ == "__main__":
    main()