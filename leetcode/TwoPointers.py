def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else: 
            right -= 1
    return [-1, -1]

print(two_sum_sorted([2, 7, 11, 15], 9))