def process(arr):
    new_arr = []
    length = len(arr)
    for i in range(3 * length):
        if i // length == 1:
            new_arr.append(arr[i % length] + " " * length + arr[i % length])
        else:
            new_arr.append(arr[i % length] * 3)

    return new_arr


star = ["***", "* *", "***"]
n = int(input())
count = 0
while n != 1:
    n //= 3
    count += 1

for _ in range(count - 1):
    star = process(star)

for row in star:
    for char in row:
        print(char, end="")
    print()