nums = [1,3,5,6]
target = int(input())

try:
    print(nums.index(target))
except ValueError:
    nums.append(target)
    nums = sorted(nums)
    print(nums.index(target))
