n=int(input("N:"))
m=int(input("M:"))
x=int(input("X:"))
mat=[]
for i in range(n):
    r=[]
    for j in range(m):
        r.append(int(input()))
    mat.append(r)    
print("result")
for i in mat:
    if x in i:
        print(1)
        break
    else:
        print(0)
        break
        
