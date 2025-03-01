# https://www.acmicpc.net/problem/25497 - 기출 연계마스터 임스

"""
1. dict 이용
- 딕셔너리를 사용하여 스킬 수를 직관적으로 관리. 스킬이 다양해지거나 복잡해져도 코드 확장이 용이하나, 스택 구조 등을 다뤄야하는 경우 추가 로직 필요.
- 접근 및 수정 면에서, table["L"] += 1 또는 table["L"] -= 1은 O(1) 이고 조회는 항상 O(1).
- "L"과 "S"라는 고정된 키를 사용하며, 정수 값만 저장하므로 추가적인 메모리 사용은 거의 없다. O(1), 상수 공간 사용.
- 조회 및 갱신이 O(1)로 일정하기 때문에 대규모 데이터에서 효율적.

2. deque 이용
- table["L"] += 1 또는 table["L"] -= 1은 O(1).
- 탐색("L" in stack)은 최악의 경우 O(k), k는 stack의 크기. # 탐색이 빈번한 경우 피할 것
- 실제로 남아 있는 스킬들을 stack에 저장하므로, 메모리 사용량은 스킬의 실제 개수와 비례. O(k), k는 저장된 스킬의 개수.

3. update
- 각 스킬에 대해 단일 연산 O(1)을 수행.
- 전체 시간 복잡도 : O(n), n은 입력 스킬 문자열의 길이.
효율성: L과 S를 카운터로 관리하여 탐색이나 정렬 없이 스킬 개수를 추적.
최적화: 메모리 사용량이 O(1)로 고정.
대규모 입력에서도 성능이 뛰어남.
"""


# Dictionaty - hashtable
n = int(input())
skills = input()

table = {"L": 0, "S": 0}
cnt = 0

for i in skills:

    # 사전 기술
    if i == "S":
        table["S"] += 1
    elif i == "L":
        table["L"] += 1

    # 본 기술
    elif i == "R":
        if table["L"] > 0:
            table["L"] -= 1
        else:
            break
    elif i == "K":
        if table["S"] > 0:
            table["S"] -= 1
        else:
            break

    else:  # 일반공격
        cnt += 1

print(cnt)


# Deque - stack
from collections import deque

cnt = 0
stack = deque()

for i in skills:
    if i == "S" or i == "L":
        stack.append(i)

    elif i == "R":
        if "L" in stack:
            stack.remove("L")  # stack.pop() X!!
            cnt += 1
        else:
            break
    elif i == "K":
        if "S" in stack:
            stack.remove("S")
            cnt += 1
        else:
            break
    else:
        cnt += 1

print(cnt)


# Update
L, S = 0, 0
cnt = 0

for i in skills:
    if i == "S":
        S += 1
    elif i == "L":
        L += 1
    elif i == "R":
        if L > 0:
            L -= 1
            cnt += 1
        else:
            break
    elif i == "K":
        if S > 0:
            S -= 1
            cnt += 1
        else:
            break
    else:
        cnt += 1

print(cnt)
