import sys
def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    h = [int(x) for x in data[1:]]
  
    if n == 2:
        print(abs(h[1] - h[0]))
        return

    prev2 = 0               
    prev1 = abs(h[1] - h[0]) 
    
    for i in range(2, n):
        cost_from_prev1 = prev1 + abs(h[i] - h[i-1])
        cost_from_prev2 = prev2 + abs(h[i] - h[i-2])
        current_cost = min(cost_from_prev1, cost_from_prev2)
        prev2 = prev1
        prev1 = current_cost
    print(prev1)
if __name__ == '__main__':
    solve()
