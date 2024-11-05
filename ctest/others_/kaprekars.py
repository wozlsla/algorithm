""" Kaprekar's Constant
num 매개변수는 최소 두 개의 고유한 숫자가 있는 4자리 숫자이다. 프로그램은 숫자에 대해 다음 루틴을 수행한다.
- 숫자를 내림차순과 오름차순으로 정렬한다. (0을 추가하여 4자리 숫자에 맞춤) 
- 더 작은 숫자에서 더 큰 숫자를 뺀다. 
- 이전 단계를 반복한다.
이 루틴을 수행하면 항상 고정된 숫자인 6174가 나온다(7641-1467 = 6174).
프로그램은 6174에 도달할 때까지 이 루틴을 수행해야 하는 횟수를 반환해야 한다.

예를 들어, num이 3524인 경우 다음 단계 때문에 프로그램은 3을 반환해야 한다.
1) 5432 - 2345 = 3087
2) 8739 - 9378 = 8352
3) 8532 - 2358 = 6174

예시
입력: 2111, 출력: 5
입력: 9831, 출력: 7
"""

# num = int(input())
num = 3524


def kaprekars(num):
    cnt = 0

    while num != 6174:
        n = str(num).zfill(4)
        asce = "".join(sorted(n))
        # desc = "".join(sorted(n, reverse=True)) # O(n log n)
        desc = asce[::-1]  # O(n)
        num = int(desc) - int(asce)
        cnt += 1

    return cnt


print(kaprekars(num))


"""
desc = "".join(sorted(n, reverse=True))
문자열 n을 정렬하여 큰 순서대로 재배열한 후, join을 사용해 다시 문자열로 합칩니다.
sorted 함수는 n의 모든 문자를 정렬하기 때문에 O(n log n) 복잡도를 가집니다.

desc = asce[::-1]
이미 정렬된 asce 문자열을 역순으로 뒤집는 방식입니다.
이 경우는 정렬이 필요 없으므로 단순히 문자열을 뒤집기만 하여 O(n) 복잡도를 가집니다.

카프리카 수 : https://codingdojang.com/scode/644?orderby=time&langby=python
"""
