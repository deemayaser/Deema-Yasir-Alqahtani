age = int(input("enter your age:"))
day = (input("enter day:").capitalize())

if age < 12:
    price=20
elif 12 <= age <= 17:
    price=35
elif 18 <= age <= 59:
    price=50       
elif age >= 60:
    price=25

if day == "Tuesday":
    price = price - 10    
    
    if price < 10:
        price = 10

print(f"Your ticket price is: {price}" )