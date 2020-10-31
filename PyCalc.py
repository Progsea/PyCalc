def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

print("What do you want to do? Add, subtract, multiply, or divide (a, s, m, d)?")
typeOfOperator = input()

if typeOfOperator == "a":
    print("Ok, what is your first number?")
    num1 = int(input())
    print("What is your second number?")
    num2 = int(input())
    print(str(num1) + " + " str(num2) + " is equal to " + str(add(num1, num2)))
    input()
    exit()
elif typeOfOperator == "s":
    print("Ok, what is your first number?")
    num1 = int(input())
    print("What is your second number?")
    num2 = int(input())
    if num1 < num2:
      print(str(num1) + " - " str(num2) + " is equal to " + str(sub(num2, num1)))
      input()
      exit()
    elif num1 >= num2:
      print(str(num1) + " + " str(num2) + " is equal to " + (sub(num1, num2)))
      input()
      exit()
    else:
      print("Something went wrong...")
      input()
      exit()

elif typeOfOperator == "m":
    print("Ok, what is your first number?")
    num1 = int(input())
    print("What is your second number?")
    num2 = int(input())
    print(str(num1) + " + " str(num2) + " is equal to " + str(mul(num1, num2)))
    input()
    exit()
elif typeOfOperator == "d":
    print("Ok, what is your first number?")
    num1 = int(input())
    print("What is your second number?")
    num2 = int(input())
    if num1 < num2:
        print("Output: " + str(div(num2, num1)))
        input()
        exit()
    elif num1 >= num2:
        print("Output: " + str(div(num1, num2)))
        input()
        exit()
    else:
        print("Something went wrong...")
        input()
        exit()
else:
    print("Wrong operator...")
    input()
    exit()
