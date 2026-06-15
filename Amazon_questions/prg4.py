count = 0
s = input("Enter:")
t = input("Enter:")
if len(s) > len(t):
    count += len(s) - len(t)
elif len(s) < len(t):
    count += 1
else:
    if s == t:
        count = 0
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
print(count)
