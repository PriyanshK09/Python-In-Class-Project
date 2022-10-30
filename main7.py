#Sum Of all numbers divisible by 3 in a given list

total = 0
lst1 = [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 17, 18]
for num in lst1:
    if num % 3 == 0:
        total += num
print(total)