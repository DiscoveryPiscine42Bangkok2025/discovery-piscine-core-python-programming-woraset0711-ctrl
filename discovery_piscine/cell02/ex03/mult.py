#!/usr/bin/env python3

# 1. รับค่าตัวเลข 2 ตัว และแปลงเป็น int ทันที
try:
    print("Enter the first number:")
    n1 = int(input())
    print("Enter the second number:")
    n2 = int(input())

    # 2. คำนวณผลลัพธ์
    res = n1 * n2

    # 3. แสดงรูปแบบการคูณ
    print(f"{n1} x {n2} = {res}")

    # 4. เช็คเงื่อนไขผลลัพธ์
    if res > 0:
        print("The result is positive.")
    elif res < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative.")

except EOFError:
    pass
except ValueError:
    print("Please enter only numbers.")