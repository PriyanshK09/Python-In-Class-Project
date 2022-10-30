#Program to Display only those numbers
#from a List that satisfy following condition

#Number must be divisible by 5
#If the number is Greater than 150 then skip it and move to next Number
#If the number is Greater than 500 then stop the loop

number = [12, 75, 150, 180, 145]
for i in number:
    if i > 150:
        continue
    elif i > 500:
        break
    elif i%5==0:
        print(i)
    
