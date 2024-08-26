a : int = 5
b : int = 3
result : int = 0

operation : int = input("Enter operation (+, -, *, /): ")

if operation == "+" :
    result=a+b
    print(f"Sum of {a} and {b} is {result}")
elif operation == "-"  :
    result=a-b
    print(f"difference of {a} and {b} is {result}")
elif operation == "*"  :
    result=a*b
    print(f"Product of {a} and {b} is {result}")
elif operation == "/"  :
    result=a/b
    print(f"Division of {a} by {b} is {result}")
else :
    print("error")