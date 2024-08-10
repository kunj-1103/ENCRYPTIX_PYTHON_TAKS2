def add(x,y):
    return x+y

def subract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

print("select operation")
print("1 Add")
print("2 Subract")
print("3 Mutliply")
print("4 Divide")

while True:
    choice=input("Enter Choice(1/2/3/4:")

    if choice in('1','2','3','4'):
        try:
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
        except ValueError:
            print("Invalid input")
            continue
        if choice=='1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice=='2':
            print(num1, "-", num2, "=", subract(num1, num2))

        elif choice=='3':
             print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice=='4':
            print(num1, "/", num2, "=", divide(num1, num2))

        next_cal=input("lets do next calculation?(yes/no:")
        if next_cal=="no":
            break
        else:
            print("Invalid Input")
            
