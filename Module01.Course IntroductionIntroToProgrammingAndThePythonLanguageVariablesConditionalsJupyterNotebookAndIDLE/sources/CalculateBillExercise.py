#set variables from user input
bill = float(input("How much is the bill? "))
tax = float(input("What is the tax percentage? "))
tip = float(input("What is the tip percentage? "))

#calculate the tax
taxAmount = bill * tax / 100
total = bill + taxAmount

#calculate the tip
tipAmount = total * tip / 100
total += tipAmount

#round the total to 2 digits after the decimal point
total = round(total, 2)

#print the total
print("The total is $", total)