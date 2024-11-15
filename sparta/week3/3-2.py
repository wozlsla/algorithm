"""
문제 설명:
주어진 정수 배열에서 모든 가능한 순열을 생성하는 프로그램을 작성하세요.
배열에는 중복된 숫자가 없다고 가정합니다.

--
1. 백트래킹을 사용하여 현재 순열에 각 숫자를 추가하고, 추가한 숫자를 다음 단계의 선택에서 제외합니다.
2. 모든 숫자가 순열에 포함되었을 때, 해당 순열을 출력하고 다른 가능성을 탐색합니다.
"""

"""
배열의 길이가 n일 때, O(n!)의 시간 복잡도 -> 순열의 모든 경우를 탐색
"""


def permute(nums):
    def backtrack(st=0):

        # 모든 숫자가 순열에 포함되었을 때 결과를 추가
        if st == len(nums):
            result.append(nums[:])
            return

        # 가능한 조합을 탐색
        for i in range(st, len(nums)):

            # nums[start]와 nums[i]를 교환하여 새로운 순열을 만듦
            nums[st], nums[i] = nums[i], nums[st]

            # 다음 숫자로 넘어가며 백트래킹 실행
            backtrack(st + 1)

            # 선택 취소 (원래 상태로 배열을 되돌리기 위함)
            # 다른 조합을 탐색하기 위한 필수 단계
            nums[st], nums[i] = nums[i], nums[st]

    result = []
    backtrack()
    return result


print(permute([1, 2, 3]))
