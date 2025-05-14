marks = float(input("enter your marks outof 100 : "))
if marks <= 100:
    if marks<= 33:
        print("you are failed")
    elif 33 < marks <= 80:
        print("You got good marks")
    else:
        print("you got too good marks")
else:
    print("Try again,you enter more than 100")