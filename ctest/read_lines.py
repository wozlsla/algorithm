# input_data = sys.stdin.read().splitlines()

import sys
from io import StringIO

# 입력 문자열을 시뮬레이션
sys.stdin = StringIO("push 1\npush 2\ntop\n")


"""
- input() : 표준 입력으로 한 줄을 받아 문자열로 반환
- 개행 문자를 자동으로 제거
"""
n = 3
for _ in range(n):
    print(input())


"""
- input이 파이썬 내장 함수가 아닌 sys.stdin.readline으로 덮어씌워짐
  이후 input()을 사용할 때 sys.stdin.readline처럼 작동
- input()보다 빠르게 작동하여, 많은 입력을 처리할 때 유리
- 표준 입력에서 한 줄을 읽어들이지만, input()과 달리 개행 문자를 포함하여 반환. 따라서 rstrip()으로 개행 문자를 제거해야 함
"""
input = sys.stdin.readline

n = 3
for _ in range(n):
    # print(input())
    print(input().rstrip())  # \n 제거


"""
한번에 처리
- readline() : 파일의 한줄을 읽어오는 함수 (개행문자 포함)
- readlines() : 파일의 끝까지 한번에 읽어옴. 각 줄이 개행문자가 포함되어 리스트로 저장
    ['push 1\n', 'push 2\n', 'top\n']
- read() : 파일의 끝까지 한번에 읽어오고 읽은대로 출력
    push 1
    push 2
    top
"""
commands = sys.stdin.read()
# push 1
# push 2
# top
# \n

commands = sys.stdin.read().strip()  # \n 제거
# push 1
# push 2
# top

commands = sys.stdin.read().strip().splitlines()  # list로 읽음
# ['push 1', 'push 2', 'top']
for command in commands:
    print(command)
