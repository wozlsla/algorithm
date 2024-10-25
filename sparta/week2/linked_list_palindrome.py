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
1) 중간 지점 찾기
2) + 연결 리스트의 절반 reverse
3) 비교 
"""


def is_palindrome_runner(ln):

    prev = None
    slow, fast = ln.head, ln.head

    # fast가 리스트의 끝에 도달하면, slow는 리스트의 중간에 도달
    while fast and fast.next:
        # print(f"fast: {fast.val}")
        # print(f"slow: {slow.val}")
        fast = fast.next.next

        # Python) 다중 할당
        prev, prev.next, slow = slow, prev, slow.next

        # [X] prev 와 slow가 동일한 참조가 됨
        # prev, prev.next = slow, prev
        # slow = slow.next

        # print(f"fast to: {fast.val}")
        # print(f"slow to: {slow.val}")  # 6
        # print(slow)

    # 길이가 홀수인 경우, slow는 중간 다음 노드에 위치
    if fast:
        slow = slow.next
        # print(slow, slow.val)  # 7

    # 팰린드롬 여부 확인
    while prev and prev.val == slow.val:
        slow, prev = slow.next, prev.next

    # print(prev)
    return not prev


from structures import LinkedList

ln = LinkedList()

# ln.append(1)
# ln.append(2)
# ln.append(3)
# ln.append(4)
# ln.append(5)
# ln.append(6)
# ln.append(7)  # slow
# ln.append(8)
# ln.append(9)
# ln.append(10)
# ln.append(11)

re = is_palindrome_runner(ln)
print(re)
