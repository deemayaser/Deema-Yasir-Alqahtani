age = int(input("enter your age:"))
job = (input("Do you have a job?").capitalize())
income = int(input("enter your income:"))

if 21 <= age <=65:
    if job == "Yes":
        if income >= 5000:
            print("Loan Approved")
        elif  3000 <= income <= 4999:
            print("Approved with conditions")
        elif income < 3000:
            print("Rejected: Low Income")   

    else:
        print("Rejected: No Job")  

else:
    print("Rejected: Age not eligible")