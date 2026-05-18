a = int(input("enter first triangle side:"))
b = int(input("enter second triangle side:"))
c = int(input("enter third triangle side:"))

if a == b:
    if b == c:
       print("triangle is Equilateral")
    else:
       print("triangle is Isosceles")

elif b == c:
   print("triangle is Isosceles")

elif a == c:
   print("triangle is Isosceles")

else:
   print("triangle is scalene")      
        
   