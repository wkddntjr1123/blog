from sys import stdin

input = stdin.readline

n = int(input())

attendance = set()
for _ in range(n):
    name, state = input().rstrip("\n").split()
    if state == "enter":
        attendance.add(name)
    else:
        attendance.remove(name)
print("\n".join(sorted(attendance, reverse=True)))