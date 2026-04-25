#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) > 1:
        params = sys.argv[1:]
        
        found_any = False
        for p in params:
            if not p.endswith("ism"):
                print(f"{p}ism")
                found_any = True

        if not found_any:
            pass
            
    else:
        print("none")

if __name__ == "__main__":
    main()