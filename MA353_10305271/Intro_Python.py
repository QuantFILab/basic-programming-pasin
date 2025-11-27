#----การนำเข้าข้อมูล ด้วยคำสั่ง input()
#x = int(input("x = "))
#z = x + 3
#y = int(input("y = "))
#x, y = input("ใส่ตัวเลข 2 ตัว: ").split()
#print(x, y)
#z = int(x) + int(y)
#print(f"z = {z}")
#======================================

#----คำตอบของสมการ a*x^2 + b*x + c = 0
#a, b, c = input("a, b, c = ").split()
#a, b, c = int(a), int(b), int(c)
#x1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
#x2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
#print(f"คำตอบของสมการคือ {x1} และ {x2}")
#======================================


def result_of_polynomial(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    x2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    return x1, x2

xx1, xx2 = result_of_polynomial(6, 4, 1)
print(f"คำตอบของสมการคือ {xx1} และ {xx2}")