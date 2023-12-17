from typing import TypeVar, Generic, Dict
from app.services.cache_system.DoublyLinkedList import DoublyLinkedList, Node

from app.services.cache_system.EvictionStrategy import EvictionStrategy

K = TypeVar('K')
V = TypeVar('V')


class Cache(Generic[K, V]):
    def __init__(self, limit: int, eviction_strategy: EvictionStrategy[K, V]) -> None:
        self.limit = limit
        self.eviction_strategy = eviction_strategy
        self.cache_map = {}  # Maps keys to nodes
        self.linked_list = DoublyLinkedList[K, V]()

    def start_cache(self, max_limit: int) -> None:
        self.max_limit = max_limit

    def add(self, key: K, value: V) -> None:
        if len(self.cache_map) >= self.limit:
            self.eviction_strategy.apply(self.linked_list, self.cache_map)

        new_node = Node(key, value)
        self.linked_list.add_to_front(new_node)
        self.cache_map[key] = new_node

    def get(self, key: K) -> V:
        if key not in self.cache_map:
            return

        node = self.cache_map[key]
        self.linked_list.move_to_front(node)
        return node.value

    def remove(self, key: K) -> None:
        if key not in self.cache_map:
            return

        node = self.cache_map[key]
        self.linked_list.remove_node(node)
        del self.cache_map[key]