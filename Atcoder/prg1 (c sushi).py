import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    n = int(data[0])
    m = int(data[1])
    a = [int(x) for x in data[2 : 2 + n]]
    b = [int(x) for x in data[2 + n : 2 + n + m]]
    
    a.sort()
    b.sort()
    
    count = 0
    b_idx = 0
    
    for item in a:
        if b_idx < m and (item * 2) >= b[b_idx]:
            count += 1
            b_idx += 1
            
    print(count)

if __name__ == '__main__':
    solve()
