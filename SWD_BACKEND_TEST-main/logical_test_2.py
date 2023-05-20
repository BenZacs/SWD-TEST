
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""
def int_to_roman(num):
    num = int(num)
    converter = (
        ("M", 1000),
        ("CM",900),
        ("D", 500),
        ("CD", 400),
        ("c", 100),
        ("XC", 90),
        ("L", 50),
        ("XXX", 30),
        ("XX", 20),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1)
    )
    result = ""
    for roman, value in converter:
        while num >= value:
            num -= value
            result += roman
    return result

num = input("Enter number: ")
roman = int_to_roman(num)
print(f"Roman nuber is: {roman}")