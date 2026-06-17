arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)
mid = n // 2

i = 0
j = mid
while i < j and j < n:
    if arr[i] <= arr[j]:
        i += 1
    else:
        temp = arr[j]
        k = j
        while k > i:
            arr[k] = arr[k - 1]
            k -= 1

        arr[i] = temp
        i += 1
        j += 1
        mid += 1

print(arr)
