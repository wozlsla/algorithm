import sys

input = sys.stdin.readline

n = int(input())
pw = []

for _ in range(n):
    s = input()
    if s == s[::-1]:
        print(len(s), s[len(s) // 2])
        break  # 조건을 일찍 만족할수록 더 빠르게 종료
    elif s not in pw and s[::-1] not in pw:
        pw.append(s)
    else:
        print(len(s), s[len(s) // 2])
        break


## 다른 풀이
# input 을 list로 즉시 변환
stack = [input() for _ in range(n)]
stack_i = [i[::-1] for i in stack]

# 교집합 (type: set -> list) : {'las', 'sal'}
key = list(set(stack) & set(stack_i))
print(str(len(key[0])) + " " + key[0][len(key[0]) // 2])
