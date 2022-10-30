#Sum Of all numbers divisible by 3 in a given list

total = 0
lst1 = [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 17, 18]
for num in lst1:
    if num % 3 == 0:
        total += num
print(total)

#Using "while" loop

total = 0
nums = [1, 3, 4, 6, 8, 9, 11, 13, 15, 16, 17, 18]
index = 0
while index < len(nums):
    num = nums[index]
    if num % 3 == 0:
        total += num
    index = index + 1
print(total)