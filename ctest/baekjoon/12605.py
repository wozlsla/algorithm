import sys
from io import StringIO

sys.stdin = StringIO("3\nthis is a test\nfoobar\nall your base\n")


# 표준 입력의 `모든 줄`을 한 번에 읽어들이는 함수
lines = sys.stdin.readlines()

n = int(lines[0].strip())

for i in range(1, n + 1):
    s = lines[i].strip().split()
    s = " ".join(s[::-1])  # .join(reversed(s))
    print(f"Case #{i}: {s}")


"""
- Slicing
    리스트의 복사본을 생성하면서 순서를 뒤집음 (새로운 리스트를 생성)
    원본 리스트의 길이에 따라 메모리 사용량 증가
- Reverse
    원본 리스트를 변경하지 않고, 뒤집어진 순서의 요소를 이터레이터 형태로 반환
    새로운 리스트를 생성하지 않아 큰 리스트 일수록 메모리 효율이 좋다
        (리스트를 복사하지 않고 이터레이터를 반환하기 때문에, O(1).
        그러나 리스트 요소에 접근할 때마다 하나씩 뒤에서 앞으로 가져오는 연산이 필요하므로, 
        최종적으로 모든 요소를 처리하는 데 걸리는 시간 복잡도는 O(n))

둘 다 리스트의 크기가 n일 때 O(n)의 시간 복잡도
"""


# 다른 사람 풀이 1
n = int(sys.stdin.readline())
stack = [sys.stdin.readline() for _ in range(n)]

for i in range(n):
    print(f"Case #{i+1}: " + " ".join(stack[i].split()[::-1]))


# 다른 사람 풀이 2
for x in range(1, int(input()) + 1):
    print(f"Case #{x}: {' '.join(input().split()[::-1])}")


""" 참고 """

input = sys.stdin.readlines  # 재정의

n = input()
# ['3\n', 'this is a test\n', 'foobar\n', 'all your base\n']


lines = sys.stdin.read().strip().splitlines()
# ['3', 'this is a test', 'foobar', 'all your base']
