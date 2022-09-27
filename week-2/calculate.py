def calculate(min, max, step):
    # 請用你的程式補完這個函式的區塊
    result = 0
    for i in range(min, max + 1, step):
        result += i
    return result


calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0

assert calculate(1, 3, 1) == 6
assert calculate(4, 8, 2) == 18
assert calculate(-1, 2, 2) == 0
