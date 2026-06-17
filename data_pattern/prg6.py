def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


x = int(input("Enter X: "))
num = x + 1
while True:
    if isPrime(num):
        print("Smallest prime greater than X is:", num)
        break
    num += 1
