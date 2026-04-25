#!/usr/bin/env python3
import sys
def downcase_it(text):
    """ฟังก์ชันรับสตริงแล้วคืนค่ากลับเป็นตัวพิมพ์เล็กทั้งหมด"""
    return text.lower()

def main():
    if len(sys.argv) > 1:
        for param in sys.argv[1:]:
            result = downcase_it(param)
            print(result)
    else:
        print("none")

if __name__ == "__main__":
    main()