# File: DoublyLinkedList.py

from typing import TypeVar, Generic

K = TypeVar('K')
V = TypeVar('V')


class Node(Generic[K, V]):
    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value
        self.prev = None  # Previous node in the linked list
        self.next = None  # Next node in the linked list


class DoublyLinkedList(Generic[K, V]):
    def __init__(self) -> None:
        self.head = None  # Head of the linked list
        self.tail = None  # Tail of the linked list

    def add_to_front(self, node: Node[K, V]) -> None:
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def move_to_front(self, node: Node[K, V]) -> None:
        if node == self.head:
            return

        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node

    def remove_node(self, node: Node[K, V]) -> None:
        if not node:
            return

        if node.next:
            node.next.prev = node.prev

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

    def remove_last(self) -> K:
        if not self.tail:
            raise ValueError("Cannot remove from an empty list")

        key_to_remove = self.tail.key

        if self.head == self.tail:
            del self.tail
            self.head = self.tail = None
        else:
            previous = self.tail.prev
            del self.tail
            self.tail = previous
            self.tail.next = None

        return key_to_remove