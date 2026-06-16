import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    a = [int(x) for x in input_data[1:]]
    
    c1, c2, c3 = a.count(1), a.count(2), a.count(3)
    dp = {(0, 0, 0): 0.0}

    for k in range(c3 + 1):
        for j in range(c2 + c3 + 1 - k):
            for i in range(c1 + c2 + c3 + 1 - j - k):
                if i == 0 and j == 0 and k == 0:
                    continue
                
                total = i + j + k
                if total > N:
                    continue
                
                res = N / total
                if i > 0: res += (i / total) * dp[(i - 1, j, k)]
                if j > 0: res += (j / total) * dp[(i + 1, j - 1, k)]
                if k > 0: res += (k / total) * dp[(i, j + 1, k - 1)]
                
                dp[(i, j, k)] = res

    print(f"{dp[(c1, c2, c3)]:.10f}")

if __name__ == '__main__':
    solve()
