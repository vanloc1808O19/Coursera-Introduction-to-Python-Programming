number = input("Input an integer ")

#try to cast the input
try:
    number = (int)(number)
#catch the raised exception if there is an error, i.e. it can't be casted
except ValueError as e:
    print("Your input is not an integer.")
    print(e)
#otherwise, there is no error, i.e. the input is an integer
else:
    print(number, "is indeed an integer.")