n = int(input("Enter number of lines: "))

for i in range(n):
    s = input("Enter line: ")

    freq = {}

    for ch in s:
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1

    max_freq = max(freq.values())

    result = []
    for ch in range(ord('A'), ord('Z') + 1):
        if freq.get(chr(ch), 0) == max_freq:
            result.append(chr(ch))

    for ch in range(ord('a'), ord('z') + 1):
        if freq.get(chr(ch), 0) == max_freq:
            result.append(chr(ch))

    print("".join(result))
