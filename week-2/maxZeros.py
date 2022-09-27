def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    cnt = 0
    max_cnt = 0
    for i in nums:
        if i == 0:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 0
    return max(max_cnt, cnt)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3

assert(maxZeros([0, 1, 0, 0]) == 2)
assert(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) == 4)
assert(maxZeros([1, 1, 1, 1, 1]) == 0)
assert(maxZeros([0, 0, 0, 1, 1]) == 3)
