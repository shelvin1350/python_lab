a=int(input("Enter a number: "))
b=int(input("Enter another number: "))

ch=int(input("Enter the operation you need:  \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division"))

if ch == 1:
    c = a+b;
    
elif ch == 2:
    c = a - b
    
elif ch == 3:
    c = a * b
    
elif ch == 4:
    c = a / b
    
print("The result is" + str(c))