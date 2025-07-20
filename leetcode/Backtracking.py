# todas a permutações de uma lista
def generate_permutations(nums):
    result = []
    def backtrack(current_permutation, remaining_nums):
        if not remaining_nums:
            result.append(list(current_permutation))
            return
        for i in range(len(remaining_nums)):
            num = remaining_nums[i]
            current_permutation.append(num)
            backtrack(current_permutation, remaining_nums[:i] + remaining_nums[i+1:])
            current_permutation.pop()
            
    backtrack([], nums)
    return result

print(generate_permutations([1, 2, 3]))
