def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def multi(num1,num2):
    return num1*num2
def divi(num1,num2):
    return num1/num2
def modu(num1,num2):
    return num1%num2
print("Welcome to Python Calculator.")
print("Please note the following choices:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
operator = int(input("Enter your choice of operator 1,2,3,4: "))
if operator==1:
    print("Addition = ", add(num1,num2))
elif operator==2:
    print("Subtraction = ", sub(num1,num2))
elif operator==3:
    print("Multiplication = ", multi(num1,num2))
elif operator==4:
    print("Division = ", divi(num1,num2))
elif operator==5:
    print("Modulus = ", modu(num1,num2))
else:
    print("Please enter a valid operator.")
