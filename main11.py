def myFunction(listOfPerson):
    num1=0
    num2=0
    
    for i in listOfPerson:
        if i<5:
            num1=num1+1
            
        else:
            num2=num2+1
    return num1,num2

listOfPerson = ["Atul", "Shubham", "Anurag", "Rahul", "Dev", "Rpy"]
num1,num2=len(listOfPerson)
print(num1)
print(num2)