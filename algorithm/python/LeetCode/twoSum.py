nums = [3,2,4]
target = 6

for key, val in enumerate(nums):
    needle = target - val
    try:
        answer = nums.index(needle)
        if answer == key:
            continue
        print([key, answer])
    except ValueError:
        continue
