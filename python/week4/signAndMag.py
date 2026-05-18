num = int(input("enter number:"))

if num < -100:
    print("Negative Large")
elif 0 > num >= -100:
    print("Negative Small")
elif num == 0:
    print("Zero")
elif 0 < num <= 100:
    print("Positive Small")
elif num > 100:
    print("Positive Large")            

