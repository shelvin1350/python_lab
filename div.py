sum = 0
for i in range(100, 200):
    if i%7 == 0:
        print(i)
        sum = sum + i;
    
print("Sum of the numbers which are divisible by 7: " + str(sum))