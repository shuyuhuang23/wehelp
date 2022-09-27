def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    if len(nums) < 2:
        raise ValueError('Length of list should be greater than 1.')

    if len(nums) == 2:
        return nums[0] * nums[1]

    max_nums = [min(nums[0], nums[1]), max(nums[0], nums[1])]
    min_nums = [min(nums[0], nums[1]), max(nums[0], nums[1])]

    for i in range(2, len(nums)):
        num = nums[i]
        if num >= max_nums[1]:
            max_nums[0] = max_nums[1]
            max_nums[1] = num
        elif num > max_nums[0]:
            max_nums[0] = num
        elif min_nums[0] >= num:
            min_nums[1] = min_nums[0]
            min_nums[0] = num
        elif min_nums[1] > num:
            min_nums[1] = num

    return max(max_nums[0] * max_nums[1], min_nums[0] * min_nums[1])


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10

assert maxProduct([5, 20, 2, 6]) == 120
assert maxProduct([10, -20, 0, 3]) == 30
assert maxProduct([10, -20, 0, -3]) == 60
assert maxProduct([-1, 2]) == -2
assert maxProduct([-1, 0, 2]) == 0
assert maxProduct([5, -1, -2, 0]) == 2
assert maxProduct([-5, -2]) == 10
