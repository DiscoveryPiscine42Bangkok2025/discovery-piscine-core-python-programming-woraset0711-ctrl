#!/usr/bin/env python3
import sys
def shrink(text):
    print(text[:8])

def enlarge(text):
    needed = 8 - len(text)
    print(text + ('Z' * needed))

def main():
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                shrink(arg)
            elif len(arg) < 8:
                enlarge(arg)
            else:
                print(arg)
    else:
        print("none")

if __name__ == "__main__":
    main()