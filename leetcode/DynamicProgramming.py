# Fibonacci com memorization
memo = {}
def fib_dp(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    result = fib_dp(n - 1) + fib_dp(n - 2)
    memo[n] = result
    return result

print(fib_dp(3))