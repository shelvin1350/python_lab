num_rows = int(input("Enter the number of rows for the pyramid: "))

for i in range(1, num_rows + 1):
    
    for j in range(num_rows - i):
        print(" ", end="")

    for k in range(1, i + 1):
        print(k, end="")
    
    for l in range(i - 1, 0, -1):
        print(l, end="")

    print()