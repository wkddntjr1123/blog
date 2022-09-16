from sys import stdin

input = lambda: stdin.readline().rstrip()


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class DoubleLinkedList:
    def __init__(self, s):
        self.head = None
        self.cursor = None

        for char in s:
            newNode = Node(char)
            if not self.head:
                self.head = newNode
                self.cursor = newNode
                continue
            newNode.left = self.cursor
            self.cursor.right = newNode
            self.cursor = newNode
        self.tail = Node(None)
        self.tail.left = newNode
        newNode.right = self.tail
        self.cursor = self.tail

    def L(self):
        if self.cursor is self.head:
            return
        self.cursor = self.cursor.left

    def D(self):
        if self.cursor is self.tail:
            return
        self.cursor = self.cursor.right

    def B(self):
        if self.cursor is self.head:
            return
        delNode = self.cursor.left
        if delNode is not self.head:
            self.cursor.left = delNode.left
            delNode.left.right = self.cursor
        else:
            self.head = self.cursor
        del delNode

    def P(self, value):
        newNode = Node(value)
        if self.cursor is not self.head:
            prevNode = self.cursor.left
            prevNode.right = newNode
            newNode.left = prevNode
        else:
            self.head = newNode
        self.cursor.left = newNode
        newNode.right = self.cursor

    def stringify(self):
        cur = self.head
        result = []
        while cur.value:
            result.append(cur.value)
            cur = cur.right
        return "".join(result)


linkedList = DoubleLinkedList(input())
for _ in range(int(input())):
    op = input()
    if op == "L":
        linkedList.L()
    elif op == "D":
        linkedList.D()
    elif op == "B":
        linkedList.B()
    else:
        _, value = op.split()
        linkedList.P(value)
print(linkedList.stringify())