def twoSum(nums, target):
    # your code here
    for i, element in enumerate(nums):
        lack = target - element
        if lack in nums:
            return [i, nums.index(lack)]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9

assert result == [0, 2]
