arr=list(map(int,input().split()))
key=int(input("key:"))
if key in arr:
    print(arr.index(key))
else:
    print(0)
