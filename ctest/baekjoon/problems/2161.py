from collections import deque

# n = int(input())
n = 7

q = deque([i for i in range(1, n + 1)])

li = []

while len(q) != 1:
    li.append(q.popleft())
    q.append(q.popleft())  # q.rotate(-1) : 첫 번째 요소를 끝으로 보냄

# * : unpacking 연산자
print(*li, q.pop())
