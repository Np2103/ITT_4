n = int(input("Enter number: "))
num = 1
length = 1

while num % n != 0:
    num = num * 10 + 1
    length += 1

print("Shortest number of 1's:")
print(num)
print("Length:", length)
