def tour(petrol, distance):
    start = 0
    balance = 0
    deficit = 0

    for i in range(len(petrol)):
        balance += petrol[i] - distance[i]

        if balance < 0:
            start = i + 1
            deficit += balance
            balance = 0

    if balance + deficit >= 0:
        return start

    return -1
