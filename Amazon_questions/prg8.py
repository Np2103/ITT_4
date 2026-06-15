def maximumSumRectangle(matrix):
    r = len(matrix)
    c = len(matrix[0])

    ans = float('-inf')

    for left in range(c):
        temp = [0] * r

        for right in range(left, c):
            for i in range(r):
                temp[i] += matrix[i][right]

            cur = temp[0]
            best = temp[0]

            for i in range(1, r):
                cur = max(temp[i], cur + temp[i])
                best = max(best, cur)

            ans = max(ans, best)

    return ans
