# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/description/ - 2231.Largest Number After Digit Swaps By Parity


# 문제 조건 잘못 이해 함
# "Return the !! largest possible value !! of num after any number of swaps."
class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int, str(num)))
        N = [0] * len(num)

        even = [0, 0]
        odd = [0, 0]
        for i, n in enumerate(num):
            if n == 0:
                N[i] = n
            elif n % 2 == 0:  # 짝수
                if even[0] == 0:
                    N[i] = n
                    even[0] += 1
                    even[1] = i
                else:
                    N[even[1]], N[i] = n, N[even[1]]
                    even[0] = 0
            else:  # 홀수
                if odd[0] == 0:
                    N[i] = n
                    odd[0] += 1
                    odd[1] = i
                else:
                    N[odd[1]], N[i] = n, N[odd[1]]
                    odd[0] = 0

        return int("".join(map(str, N)))


num = 1234
num = 65875
num = 60
num = 64
print(Solution().largestInteger(num))


"""
# 첫 번째 솔루션 (더 느림) : int("".join(map(str, num)))
- 각 숫자를 다시 문자열로 변환 (map(str, num))
- 문자열들을 합치는 작업 (join)
- 최종적으로 다시 정수로 변환 (int())
[1, 2, 3] -> ["1", "2", "3"] -> "123" -> 123

# 두 번째 솔루션 : res * 10 + pop값
0 -> 1 -> 12 -> 123 # 단순 산술 연산
"""


class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int, str(num)))
        even, odd = [], []

        for n in num:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        even.sort()
        odd.sort()

        # 아래 풀이보다 오래걸림
        for i in range(len(num)):
            if num[i] % 2 == 0:
                num[i] = even.pop()
            else:
                num[i] = odd.pop()
        return int("".join(map(str, num)))


class Solution:
    def largestInteger(self, num: int) -> int:
        num = list(map(int, str(num)))
        even, odd = [], []

        for n in num:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        even.sort()
        odd.sort()

        res = 0
        for i in range(len(num)):
            if num[i] % 2 == 0:
                # 예: res가 12이고 even.pop()이 3일 때
                # res * 10 = 120이 되고 + 3 = 123이 됨
                # 이렇게 자릿수를 하나씩 늘려가며 숫자를 만듦
                res = res * 10 + even.pop()
            else:
                res = res * 10 + odd.pop()
        return res
