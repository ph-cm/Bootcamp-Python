arr = [1, 2, 3, 4, 5]
prefix_sum = [0] * (len(arr) + 1) 
for i in range(len(arr)):
    prefix_sum[i+1] = prefix_sum[i] + arr[i]

print(prefix_sum)

# somar um sub conjunto do array determinado
sum_subarray = prefix_sum[4] - prefix_sum[1]
print(sum_subarray)