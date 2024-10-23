# Linked list의 palindrome 판별


def is_palindrome(ln):
    arr = []  # list 변환
    head = ln.head

    if not head:  # empty
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) > 1:
        first = arr.pop(0)
        last = arr.pop()
        if first != last:
            return False

    return True


""" Runner 
연결 리스트의 절반을 뒤집고 비교 
1) 중간 지점 찾기
2) 연결 리스트의 후반부 반전
3) 비교
"""
