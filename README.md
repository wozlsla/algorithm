# Python
- 객체 참조
- [다중 할당](https://github.com/wozlsla/algorithm/blob/5cfd6ef42b25da4ef0d89c013e091e68d925290f/sparta/week2/linked_list_palindrome.py#L44)
- [객체 재사용 (Interning)](https://github.com/wozlsla/algorithm/blob/main/python/interning.py)

</br>
</br>

# 자료구조
구현 : [structures.py](https://github.com/wozlsla/algorithm/blob/main/sparta/week2/structures.py)
  
### Linked List

- 배열은 물리적인 메모리 주소가 연속적이고, 연결리스트는 물리 메모리 주소가 연속적이지 않고 랜덤이다
- 연결 리스트의 각 노드는 데이터와 함께 다음 노드를 가리키는 포인터(참조) 역할을 하는 next 필드를 가지고 있다  
- 이 참조는 new_node의 실제 메모리 주소를 가리키고 있지만, Python에서는 C나 Go 처럼 이를 직접적으로 다루지 않고 참조로 관리
> Python : 모든 것이 객체로 취급되며, 변수는 객체의 참조를 저장  
> Go : 포인터를 사용하여 명시적으로 메모리 주소를 다룸