# 시간 초과
def solution(participant, completion):

    for i in completion:
        if i in participant:
            participant.remove(i)

    return participant.pop()


def solution(participant, completion):
    part = set(participant)

    if part != len(completion) - 1:
        participant.sort
        completion.sort

        for idx, i in enumerate(completion):
            if i != participant[idx]:
                return participant.pop(idx)

    return (part - set(completion)).pop()


def solution(participant, completion):
    from collections import Counter

    """
    Counter : 각 원소가 몇 번씩 나오는지 저장된 객체 반환
    Counter({'mislav': 2, 'stanko': 1, 'ana': 1}) <class 'collections.Counter'>

    - dictionary를 확장하고 있기 때문에, API를 그대로 다 시용 가능
      counter["mislav"] : 2
    - 산술 연산 가능
    """
    diff = Counter(participant) - Counter(completion)

    return list(diff.elements())[0]  # list(diff.keys())[0]


# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
participant = ["mislav", "stanko", "mislav", "mislav", "ana"]
completion = ["stanko", "ana", "mislav", "mislav"]
print(solution(participant, completion))
