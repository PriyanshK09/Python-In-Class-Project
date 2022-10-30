#Print First 10 Natural Numbers using While Loop

number = int(input("Please Enter any Number: "))
i = 1

print("The List of Natural Numbers from 1 to {0} are".format(number)) 

while ( i <= number):
    print (i, end = '  ')
    i = i + 1