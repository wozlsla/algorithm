from collections import deque


def test_problem_queue(n):
    deq = deque([i for i in range(1, n + 1)])

    while len(deq) > 1:
        deq.popleft()
        front = deq.popleft()
        deq.append(front)

    return deq.pop()


"""
1부터 N까지 차례대로 줄을 섰을 때, 맨 앞에 선 사람만 들여보내주고 그 다음 순서인 사람은 제일 뒤로 보내는 특이한 줄서기가 있습니다.

예를 들어 N=6인 경우, 123456 이 순서대로 줄을 서있을 것입니다. 이때 제일 먼저 1이 입장하고 남은 순서는 23456이 됩니다. 2는 두 번째 순서이므로 제일 뒤로 보내서 34562가 됩니다. 다시 3이 입장하여 4562가 되고, 4가 두 번째 순서이므로 5624가 됩니다. 5가 입장하고 246, 2가 입장하고 64, 6이 입장하여 4, 마지막으로 4가 입장하게 됩니다.

N이 주어질 때 제일 마지막으로 입장하는 숫자를 계산하는 프로그램을 작성하세요.
"""
