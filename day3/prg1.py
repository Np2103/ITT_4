
l=[]
n=int(input())
while n!=0:
    r=n%10
    l.append(r)
    n=n//10
a=sum(l)    
if len(l) !=4:
    print("Not lucky number")
elif a%3==0 or a%5==0 or a%7==0:
    print("Lucky number")
else:
    print("Not lucky number")
    
