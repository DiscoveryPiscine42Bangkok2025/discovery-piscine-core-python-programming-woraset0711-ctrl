#!/usr/bin/env python3

def average(scores_dict):
    scores = scores_dict.values()

    if not scores:
        return 0

    class_average = sum(scores) / len(scores)
    
    return class_average

if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")