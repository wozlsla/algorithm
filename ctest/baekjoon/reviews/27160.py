# https://www.acmicpc.net/problem/27160 - 할리갈리
import sys
from io import StringIO

sys.stdin = StringIO("3\nBANANA 2\nPLUM 4\nBANANA 3\n")
input = sys.stdin.readline

N = int(input())
fruit_dict = {}

for _ in range(N):
    card = input().split()

    if card[0] not in fruit_dict:
        fruit_dict[card[0]] = 0

    fruit_dict[card[0]] += int(card[1])
    fruit_dict.get(card[0], 0) += int(card[1])

print("YES") if 5 in fruit_dict.values() else print("NO")


# dict.get() 을 사용할 경우 추가적인 초기화 단계 불필요
for _ in range(N):
    key, value = input().split()
    fruit_dict.get(key, 0) += int(value)

print("YES") if 5 in fruit_dict.values() else print("NO")