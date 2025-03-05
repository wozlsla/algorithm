# https://www.acmicpc.net/problem/11561 - 징검다리


t = int(input())

for _ in range(t):

    n = int(input())

    start = 1
    end = n

    result = 0

    while start <= end:
        mid = (start + end) // 2

        # k(k+1)//2
        if ((mid + 1) * mid) // 2 <= n:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)

"""
- 주어진 징검다리의 개수 N이 있을 때, 1부터 N까지의 수 중에서 가장 많이 건널 수 있는 수 K를 찾는 것
- 두 번째 점프부터는 이전의 점프한 거리보다 1 이상 긴 거리를 뛰어야 함
- 가장 이상적으로는 처음에 한 칸 뛰고, 그 다음 두 칸, 그 다음 세 칸 뛰는 식으로 점프하는 거리를 한 칸씩 늘리는 것
    -> 징검다리를 최대로 밟을 수 있는 수 
    -> 징검다리의 수 N이 주어졌을 때, '최대로 밟을 수 있는 수를 먼저 구하고' N보다 작거나 같은지 확인.
    => 연속된 자연수의 합 : k(k+1)//2 < n
"""
