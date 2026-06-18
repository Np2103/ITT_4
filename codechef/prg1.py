import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    p = [float(x) for x in input_data[1:n+1]]
    
    dp = [0.0] * (n + 1)
    dp[0] = 1.0
    
    for i in range(n):
        current_p = p[i]
        for j in range(i + 1, -1, -1):
            heads = dp[j - 1] * current_p if j > 0 else 0.0
            tails = dp[j] * (1.0 - current_p)
            dp[j] = heads + tails

    min_heads_needed = n // 2 + 1
    ans = sum(dp[min_heads_needed:n+1])
    print(f"{ans:.10f}")

if __name__ == '__main__':
    solve()
