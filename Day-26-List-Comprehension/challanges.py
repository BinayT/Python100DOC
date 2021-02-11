# Turning the list of following numbers to their square
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# numbers_squared = [pow(num, 2) for num in numbers]
# print(numbers_squared)

with open('file1.txt', mode='r') as file1:
    file1_content = [int(nums[:-1]) for nums in file1.readlines()]

with open('file2.txt', mode='r') as file2:
    file2_content = [int(nums[:-1]) for nums in file2.readlines()]

commons_nums = [num for num in file1_content if num in file2_content]
print(sorted(commons_nums))
# for num in file1_content:
#     if num in file2_content and num not in commons_nums:
#         commons_nums.append(num)
#
# print(commons_nums)