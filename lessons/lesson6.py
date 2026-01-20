nums = [7,11,15, 9, 2]
target = 269

def two_sum(nums, target):

    n = len(nums)

    for i in range(n - 1):
        for j in range(i+1, n):
            sum = nums[i] + nums[j]
            if sum == target:
                return [i, j]

    return []

print(two_sum(nums, target))
