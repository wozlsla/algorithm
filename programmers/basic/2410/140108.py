"""
문제
문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
-> 기준 문자 x 와 그 외의 모든 문자들이 나온 총 횟수 확인

나 sol()
이해 -> 어떤 문자와 어떤 한 다른 문자가 나온 갯수가 같아질 때 분리 (빈도가 동일한 두 문자가 있을 때 문자열을 분리)
풀이 => 해시테이블에 키(문자)와 값(횟수) 저장하여 비교

예시
s = "aaabbacbcc"  

결과 : 2 (aaabbacb cc)
내가 생각한 결과 : 1 (bbb ccc)

[ 주어진 예시 ]
s = "banana"
결과 : 3, ba - na - na

s = "abracadabra"
결과 : 6, ab - ra - ca - da - br - a

s = "aaabbaccccabba"
결과 : 3, aaabbacc - ccab - ba
(내 이해)
aaa + a: 4, bb: 2, cc: 2 
cc: 2, a: 1, b: 1
b: 1, a:1

"""


def sol(s):

    table = {}
    cnt = 0

    for char in s:
        if char not in table:
            table[char] = 1  # 문자열 추가
        else:
            table[char] += 1

        if len(table) > 1:  # 비교
            for i in table.keys():
                # 현재 문자의 빈도와 다른 문자 빈도가 같은 경우
                if table[i] == table.get(char):
                    if i != char:  # 서로 다른 문자인지 확인
                        cnt += 1  # 분리
                        table = {}  # 초기화
                        break
    # 남아 있는 문자가 있다면, 이를 하나의 분리된 부분으로 간주
    if len(table) != 0:
        cnt += 1

    return cnt


# 50min


""" 풀이 """


def solution(s):
    cnt = 0
    sav1 = 0
    sav2 = 0

    for i in s:
        if sav1 == sav2:
            cnt += 1
            a = i

        if i == a:
            sav1 += 1
        else:
            sav2 += 1
    return cnt


# ... ... ....
s = "aaabbacbcc"  # aaabbacb cc -> 2 ([aaaa][bbcb] cc)
s = "aaabbacbcc"  # aaabbacbcc -> 1 (bbb ccc)
print(solution(s))
print(sol(s))


""" Queue """

from collections import deque


def solution(s):

    cnt = 0
    q = deque(s)

    while q:
        a, b = 1, 0
        x = q.popleft()

        while q:
            n = q.popleft()
            if n == x:
                a += 1
            else:
                b += 1

            if a == b:
                cnt += 1
                break
    if a != b:
        cnt += 1

    return cnt
