while True:
    print("="*40)
    print("welcome to Python Menu Driven Calculator")
    print("="*40)
    num1 = int(input("Enter your First Number:- "))
    num2 = int(input("Enter your Second Number:- "))
    print("[1] Addition(+)\n[2] Subtraction(-)\n[3] Multiplication(*)\n[4] Divison(%)")
    choise = int(input("Chose From Above:- "))
    if choise == 1:
        print("Your Addition is",num1+num2)
    elif choise == 2:
        print("Your Subtraction is",num1-num2)
    elif choise == 3:
        print("Your Multiplication is",num1*num2)
    elif choise == 4:
        print("Your Dvision is",num1/num2)
    else:
        print("Your Choise Is Invalid")
    ans = input("Do you Want To Contunue? (y/n):- ")
    ans = ans.lower()
    if ans != 'y':
        break

