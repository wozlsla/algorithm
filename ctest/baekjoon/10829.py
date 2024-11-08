import sys
from collections import deque


# 메모리 : 34184 KB, 약 68s
class Stack:

    def __init__(self):
        self.stack = deque()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            return -1
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def empty(self):
        if self.stack:
            return 0
        return 1

    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]


def main():

    input_data = sys.stdin.read().splitlines()
    commands = input_data[1:]

    stack = Stack()

    for cmd in commands:

        cmd = cmd.split()

        if cmd[0] == "push":
            stack.push(cmd[1])
        elif cmd[0] == "top":
            print(stack.top())
        elif cmd[0] == "size":
            print(stack.size())
        elif cmd[0] == "empty":
            print(stack.empty())
        elif cmd[0] == "pop":
            print(stack.pop())


# n = int(input())
main()


# 다른 사람 풀이 (메모리: 31120 KB, 약 40s)
input = sys.stdin.readline


def sol():
    stack = []
    N = int(input())

    for n in range(N):
        command = input().rstrip()
        if command == "pop":
            print(stack.pop() if stack else -1)
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            print(+(not stack))
        elif command == "top":
            print(stack[-1] if stack else -1)
        else:
            _, x = command.split()
            stack.append(x)


sol()


"""
어차피 deque 쓸 거였으면 그냥 구현하면 됐을걸...
원래 하려던 것.. (메모리 : 33164 KB, 약 40s)
"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self, val):
        self.top = None
        self.size_cnt = 0  # 스택의 크기 (list 는 len 따로 저장)

    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
        self.size_cnt += 1

    def pop(self):
        if not self.top:
            return -1
        pop_val = self.top.val
        self.top = self.top.next
        self.size_cnt -= 1
        return pop_val

    def size(self):
        return self.size_cnt

    def empty(self):
        return 0 if self.top else 1

    def top_val(self):
        if not self.top:
            return -1
        return self.top.val


def main():
    stack = Stack()

    input_data = sys.stdin.read().splitlines()
    commands = input_data[1:]

    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == "push":
            stack.push(int(cmd[1]))
        elif cmd[0] == "top":
            print(stack.top_val())
        elif cmd[0] == "size":
            print(stack.size())
        elif cmd[0] == "empty":
            print(stack.empty())
        elif cmd[0] == "pop":
            print(stack.pop())


main()
