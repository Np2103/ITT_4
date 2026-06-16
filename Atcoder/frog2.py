import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    k = int(data[1])
    h = [int(x) for x in data[2:]]
    
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(1, n):
        for step in range(1, k + 1):
            if i - step >= 0:
                cost = dp[i - step] + abs(h[i] - h[i - step])
                if cost < dp[i]:
                    dp[i] = cost
            else:
                break
                
    print(dp[n - 1])

solve()
