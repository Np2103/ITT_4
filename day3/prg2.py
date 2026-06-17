decimal = int(input("Enter a decimal number: "))
if decimal <= 0:
    print("Invalid input")
else:
    binary_str = bin(decimal)[2:]
    ones_count = binary_str.count('1')
print(f"Binary representation: {binary_str}")
print(f"Count of 1's: {ones_count}")


