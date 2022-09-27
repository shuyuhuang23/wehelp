function twoSum(nums, target) {
    // your code here
    let i;
    for (i = 0; i < nums.length; i++) {
        let idx = nums.indexOf(target - nums[i]);
        if (idx != -1) {
            return [i, idx]
        }
    }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

console.assert(JSON.stringify(twoSum([2, 11, 7, 15], 9)) === JSON.stringify([0, 2]), 'Wrong return.');