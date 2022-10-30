#Sum Of all numbers divisible by 3 in a given list
total = 0
numList = [1, 3, 4, 6, 8, 9, 11, 13, 15, 16]
index = 0
while index < len(numList):
    num = numList[index]
    if num % 3 == 0:
        total += num
print(total)