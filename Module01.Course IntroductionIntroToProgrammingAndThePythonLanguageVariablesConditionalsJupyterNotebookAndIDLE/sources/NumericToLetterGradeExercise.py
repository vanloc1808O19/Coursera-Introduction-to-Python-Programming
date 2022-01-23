#get the value from the user input
numeric = int(input("Input the grade: "))
res = 'Z'

#check if the grade is valid
if (numeric > 100 or numeric < 0):
    print("Invalid grade")
elif (numeric >= 90):
    res = 'A'
elif (numeric >= 80):
    res = 'B'
elif (numeric >= 70):
    res = 'C'
elif (numeric >= 60):
    res = 'D'
else:
    res = 'F'

print("Letter grade is:", res)