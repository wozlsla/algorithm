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
        # 노드 객체 생성, top 노드를 next로 연결
        node = Node(val, self.top)
        # top을 새로 생성한 노드로 업데이트. 스택의 맨 위를 가리키게 함
        self.top = node

    def pop(self):
        if not self.top:
            return None

        node = self.top
        # 이전 노드와의 연결을 끊음, top을 다음 노드로 업데이트
        # Python) 사용되지 않으면 메모리에서 자동으로 정리 됨 - Garbage Collection
        self.top = node.next

        return node.val

    def is_empty(self):
        return self.top is None


""" Queue """


class Queue:
    def __init__(self):
        self.front = None

    def push(self, val):
        if not self.front:
            self.front = Node(val)
            return

        node = self.front
        while node.next:
            node = node.next

        node.next = Node(val)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = node.next
        return node.val

    def is_empty(self):
        return self.front is None
