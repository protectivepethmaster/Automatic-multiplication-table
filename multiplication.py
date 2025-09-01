num = int(input("กรอกแม่สูตรคูณที่ต้องการดู: "))

b = int(input("กรอกเลขสุดท้ายที่ต้องการให้แสดงสูตรคูณ: "))


print(f"\nตารางสูตรคูณแม่ {num}")
print("-" * 25)


for i in range(1, b+1):
    result = num * i
    print(f"{num} x {i} = {result}")