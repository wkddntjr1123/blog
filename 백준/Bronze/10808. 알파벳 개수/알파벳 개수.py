s = input()
buffer = [0 for _ in range(26)]

for char in s:
    buffer[ord(char) - ord("a")] += 1

print(" ".join(map(str, buffer)))