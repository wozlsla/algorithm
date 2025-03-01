import sys

from io import StringIO

# sys.stdin = StringIO("1\n1 2\n3 4\n")

sys.stdin = StringIO(
    """5
1 2
1 1
2
1 3
2
"""
)
# input = sys.stdin.readline

# n = int(input())

# print(input().splitlines())
# print(input().strip()) # 1 2
# print(input().strip().split()) # ['1', '2']

# 1 <class 'str'>
#   <class 'str'>
# 2 <class 'str'>

# input = sys.stdin.read().strip().splitlines()
from collections import deque

input = sys.stdin.read().strip().splitlines()
# n = input()
# print(input)

cnt = s = 0
q = deque()

for i in input[1:]:

    if len(i) == 1:
        q.popleft()

    else:
        q.append(i[-1])

        # if cnt < len(q):
        #     cnt = len(q)
        # elif cnt == len(q):
        #     if s == 0 or s > int(i[-1]):
        #         s = int(i[-1])
        if cnt <= len(q):
            cnt = len(q)
            if s == 0 or s > int(i[-1]):
                s = int(i[-1])

print(cnt, s)
