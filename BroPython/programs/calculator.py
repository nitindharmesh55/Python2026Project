# Calculator;

operator = input("Enter Operator: ");
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))


if operator == "+":
    result =  num1 + num2
    print(result);
elif operator == "-":
    result =  num1 - num2
    print(result);
elif operator == "*":
    result = num1 * num2
    print(result);
elif operator == "/":
    result =  num1 / num2
    print(result);
