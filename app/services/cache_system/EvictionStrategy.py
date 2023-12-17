from typing import TypeVar, Generic, Dict

from app.services.cache_system.DoublyLinkedList import DoublyLinkedList, Node

K = TypeVar('K')
V = TypeVar('V')


class EvictionStrategy(Generic[K, V]):
    def apply(self, linked_list: DoublyLinkedList[K, V], node_map: Dict[K, Node[K, V]]) -> None:
        # raise NotImplementedError("Subclasses must implement apply method")
        pass


class LRUEvictionStrategy(EvictionStrategy[K, V]):
    def apply(self, linked_list: DoublyLinkedList[K, V], node_map: Dict[K, Node[K, V]]) -> None:
        key_to_remove = linked_list.remove_last()
        del node_map[key_to_remove]