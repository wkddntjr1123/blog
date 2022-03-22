from sys import stdin
input = stdin.readline

num_v = int(input())

def alpah_to_num(char):
    return ord(char) - (ord("A") - 1) if char != "." else -1

adj = [[] for _ in range(num_v + 1)]
for _ in range(num_v):
    v1, left, right = input().split()
    adj[alpah_to_num(v1)].append(alpah_to_num(left))
    adj[alpah_to_num(v1)].append(alpah_to_num(right))


def preorder(v):
    print(chr(v + ord("A") - 1), end="")
    if adj[v][0] != -1:
        preorder(adj[v][0])
    if adj[v][1] != -1:
        preorder(adj[v][1])

def inorder(v):
    if adj[v][0] != -1:
        inorder(adj[v][0])
    print(chr(v + ord("A") - 1), end="")
    if adj[v][1] != -1:
        inorder(adj[v][1])

def postorder(v):
    if adj[v][0] != -1:
        postorder(adj[v][0])
    if adj[v][1] != -1:
        postorder(adj[v][1])
    print(chr(v + ord("A") - 1), end="")

preorder(1)
print()
inorder(1)
print()
postorder(1)