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


""" Hash Table (Chaining) """


class HashNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, val):
        idx = self._hash_function(key)

        if self.table[idx] is None:
            self.table[idx] = HashNode(key, val, None)
        else:
            node = self.table[idx]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key, val, None)

    def get(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]

        while node is not None:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        prev = None

        while node is not None:
            if node.key == key:
                if prev is not None:
                    prev.next = node.next
                else:
                    self.table[idx] = node.next

            prev = node
            node = node.next


""" Max Heap """


class BinaryMaxHeap:
    def __init__(self):
        self.item = [None]

    def insert(self, val):
        self.items.append(val)

        now = len(self.items) - 1  # idx
        parent = now // 2

        while parent > 0:
            if self.items[now] > self.items[parent]:
                self.items[now], self.items[parent] = (
                    self.items[parent],
                    self.items[now],
                )

            now = parent
            parent = now // 2

    def extract(self):
        if len(self.items) < 2:  # [None, ...]
            return None

        # self.items[1]의 값을 참조
        root = self.items[1]  # max(head) -> return

        # 각각의 객체로 '참조를 바꾸는' 작업
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        self.items.pop()  # 제거

        self._percolate_down(1)  # 정렬

        return root

    def _percolate_down(self, now):
        largest = now
        left = 2 * now
        right = 2 * now + 1

        """
        1. 왼쪽 자식 노드가 힙의 길이보다 작고, 
           현재 노드의 값보다 크다면, largest를 왼쪽 자식 노드의 인덱스로 업데이트
        2. 오른쪽 자식 노드가 존재하고, 
           현재 가장 큰 값(largest)보다 더 큰 값을 가지고 있다면, largest를 오른쪽 자식 노드의 인덱스로 변경
        """
        if left < len(self.item) and self.items[left] > self.items[largest]:
            largest = left
        if right < len(self.item) and self.items[right] > self.items[largest]:
            largest = right

        if largest != now:
            self.items[largest], self.items[now] = self.items[now], self.items[largest]
            self._percolate_down(largest)


""" Min Heap """
# https://github.com/wozlsla/algorithm/blob/4880008bd1473d4e466c094f7c1444e69a818755/ctest/baekjoon/1927.py


class BinaryMinHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = (
                    self.items[parent],
                    self.items[cur],
                )

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        smallest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur], self.items[smallest] = (
                self.items[smallest],
                self.items[cur],
            )
            self._percolate_down(smallest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root
