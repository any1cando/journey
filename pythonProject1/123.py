a = float(input())
b = float(input())
com = input()
otv = 0
if ((type(a) == float) and (type(b) == float) and (type(com) != float and int)):
    if (com == "mod"):
        if (b == 0):
            print("Деление на 0!")
        else:
            print(float(a % b))
    if (com == "pow"):
        {
            print(float(a**b))
        }
    if (com == "div"):
            if (b == 0):
                print ("Деление на 0!")
            else:
                print(int(a / b))
    if (com == "+"):
        {
            print(float(a+b))
        }
    if (com == "-"):
        {
            print(float(a-b))
        }
    if (com == "*"):
        {
            print(float(a*b))
        }
    if (com == "/"):
        if (b == 0):
            print ("Деление на 0!")
        else:
            print(a / b)
