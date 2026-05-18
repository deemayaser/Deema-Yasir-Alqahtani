score = int(input("enter score:"))
if 0 <= score <= 100:
    if score >= 90:
        print ("your grade is A")
    elif 80<=score<=89:
        print("your grade is B")
    elif 70<=score<=79:
        print("your grade is C")
    elif 60<=score<=69:
        print("your grade is D")
    elif score < 60:
        print("your grade is F")
else:
    print("invalid score")                
           