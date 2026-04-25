#!/usr/bin/env python3

def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    temp_list = []
    for x in original_array:
        if x > 5:
            temp_list.append(x + 2)

    new_set = set(temp_list)
    
    print(original_array)
    print(new_set)

if __name__ == "__main__":
    main()