#Using While Loops Print First 10 even numbers
number = int(input("Please Enter any Number: "))
i = 1

print("The List of Even Numbers from 1 to {0} are".format(number)) 

while ( i <= number):
    print (i, end = '  ')
    i = i + 2