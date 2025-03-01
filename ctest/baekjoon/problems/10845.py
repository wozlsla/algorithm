import sys
from collections import deque

from io import StringIO

input_text = """
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""

string_io_input = StringIO(input_text)

input = string_io_input.read().strip().splitlines()
q = deque()

for cmd in input[1:]:
    cmd = cmd.split()
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "pop":
        print(q.popleft() if q else -1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty":
        print(0 if q else 1)
    elif cmd[0] == "front":
        print(q[0] if q else -1)
    elif cmd[0] == "back":
        print(q[-1] if q else -1)
