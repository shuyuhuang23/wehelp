function maxZeros(nums) {
    // 請用你的程式補完這個函式的區塊
    let cnt = 0;
    let max_cnt = 0;
    let i;
    for (i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            cnt += 1;
        } else {
            if (cnt > max_cnt) {
                max_cnt = cnt;
            }
            cnt = 0;
        }
    }
    return Math.max(max_cnt, cnt)
}

maxZeros([0, 1, 0, 0]); // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
maxZeros([1, 1, 1, 1, 1]); // 得到 0
maxZeros([0, 0, 0, 1, 1]); // 得到 3

console.assert(maxZeros([0, 1, 0, 0]) === 2, 'Wrong return.');
console.assert(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) === 4, 'Wrong return.');
console.assert(maxZeros([1, 1, 1, 1, 1]) === 0, 'Wrong return.');
console.assert(maxZeros([0, 0, 0, 1, 1]) === 3, 'Wrong return.');