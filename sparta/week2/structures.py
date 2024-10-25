""" Linked List """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        # head 를 node 변수에 할당 : 리스트의 시작점에서 탐색을 시작하겠다
        node = self.head

        # next 필드가 None인 경우 그 노드가 끝이라는 뜻
        while node.next:
            node = node.next

        # 마지막 노드의 next 필드에 새 node를 연결 : 새로운 노드를 리스트의 마지막에 추가
        node.next = ListNode(val, None)


""" Stack """


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        node = Node(val, self.top)
        self.top = node
        # self.top = Node(val, self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = node.next

        return node.val

    def is_empty(self):
        return self.top is None
