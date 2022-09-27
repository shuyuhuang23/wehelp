function maxProduct(nums) {
    // 請用你的程式補完這個函式的區塊
    if (nums.length < 2) {
        throw 'Length of list should be greater than 1.';
    }

    if (nums.length == 2) {
        return nums[0] * nums[1]
    }

    let max_nums = [Math.min(nums[0], nums[1]), Math.max(nums[0], nums[1])];
    let min_nums = [Math.min(nums[0], nums[1]), Math.max(nums[0], nums[1])];

    let i;
    for (i = 2; i < nums.length; i++) {
        let num = nums[i];
        if (num >= max_nums[1]) {
            max_nums[0] = max_nums[1];
            max_nums[1] = num;
        } else if (num > max_nums[0]) {
            max_nums[0] = num;
        } else if (min_nums[0] >= num) {
            min_nums[1] = min_nums[0];
            min_nums[0] = num;
        } else if (min_nums[1] > num) {
            min_nums[1] = num;
        }
    }
    return Math.max(max_nums[0] * max_nums[1], min_nums[0] * min_nums[1]);
}
maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([10, -20, 0, -3]) // 得到 60
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0 或 -0
maxProduct([5, -1, -2, 0]) // 得到 2
maxProduct([-5, -2]) // 得到 10

console.assert(maxProduct([5, 20, 2, 6]) === 120, 'Wrong return.');
console.assert(maxProduct([10, -20, 0, 3]) === 30, 'Wrong return.');
console.assert(maxProduct([10, -20, 0, -3]) === 60, 'Wrong return.');
console.assert(maxProduct([-1, 2]) === -2, 'Wrong return.');
console.assert(maxProduct([-1, 0, 2]) === 0, 'Wrong return.');
console.assert(maxProduct([5, -1, -2, 0]) === 2, 'Wrong return.');
console.assert(maxProduct([-5, -2]) === 10, 'Wrong return.');