from collections import deque
from sys import stdin

input = stdin.readline
s = input().rstrip()
num_op = int(input())

left = deque()
right = deque()
for char in s:
    left.append(char)

def move_start():
    global left, right
    if left:
        right.appendleft(left.pop())

def move_end():
    global left, right
    if right:
        left.append(right.popleft())

def insert_data(data):
    global left
    left.append(data)

def delete_data():
    global left
    if left:
        left.pop()

for _ in range(num_op):
    op = input().split()  # L:좌 ,D:우, B:삭제, P는 삽입
    if op[0] == "P":
        insert_data(op[1])
    elif op[0] == "L":
        move_start()
    elif op[0] == "D":
        move_end()
    else:
        delete_data()

print(*left, *right, sep="")