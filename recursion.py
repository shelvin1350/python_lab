def rec(num):
    if num > 10:
        return 0  
    else:
        return num + rec(num + 1)  
sum = rec(0)

print("The sum is", sum)
