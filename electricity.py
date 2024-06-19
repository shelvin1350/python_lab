
print(" 0-200 Rs. 0.50 per unit\n 201-400 Rs. 0.65 per unit in excess of 200 \n")
print(" 401-600 Rs 0.80 per unit excess of 400\n  601 and above Rs 1.00per unit excess of 600\n")
print(" Rs. 400, then a surcharge of 15% will be charged")

units = int(input("Enter the units used: "))

if units >= 0 and units <= 200:
     total_bill = 0.5 * units
     
elif units >= 201 and units <=400:
    total_bill = units * 0.65 

elif units >= 401:
    if units >= 401 and units <= 600:
        total_bill = units * 0.80
        total_bill = total_bill + (0.15 * total_bill)
        
    elif units >= 401 and units <= 600:
        total_bill = units * 1
        total_bill = total_bill + (0.15 * total_bill)


if(total_bill <= 100):
    total_bill = 100
print("Your total bill is " + str(total_bill))
        

    