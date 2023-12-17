import string
from typing import TypeVar
from app.services.cache_system.Cache import Cache

K = TypeVar('K')
V = TypeVar('V')

class CommandInterpreter:
    @staticmethod
    def interpret_command(cache: Cache[K, V], command: string) -> None:
        parts = command.split()

        if not parts:
            return

        operation = parts[0].lower()

        command_handlers = {
            "start_cache": CommandInterpreter.start_cache,
            "add_key_value": CommandInterpreter.add_key_value,
            "get_value": CommandInterpreter.get_value,
            "delete_key": CommandInterpreter.delete_key,
        }

        handler = command_handlers.get(operation, CommandInterpreter.invalid_command)
        handler(cache, parts)

    @staticmethod
    def start_cache(cache: Cache[K, V], parts: list) -> None:
        if len(parts) == 2 and parts[1].isdigit():
            max_limit = int(parts[1])
            cache.start_cache(max_limit)
            print(f"Started Cache with Maximum Limit {max_limit}")
        else:
            print("Invalid start_cache command")

    @staticmethod
    def add_key_value(cache: Cache[K, V], parts: list) -> None:
        if len(parts) == 3 and parts[1].isdigit() and parts[2].isdigit():
            key, value = int(parts[1]), int(parts[2])
            cache.add(key, value)
            print(f"Added Key Value Pair ({key},{value})")
        else:
            print("Invalid add_key_value command")

    @staticmethod
    def get_value(cache: Cache[K, V], parts: list) -> None:
        if len(parts) == 2 and parts[1].isdigit():
            key = int(parts[1])
            value = cache.get(key)
            message = f"Value of key {key} is {value}" if value is not None else f"OOPS! No key with {key}"
            print(message)
        else:
            print("Invalid get_value command")

    @staticmethod
    def delete_key(cache: Cache[K, V], parts: list) -> None:
        if len(parts) == 2 and parts[1].isdigit():
            key = int(parts[1])
            cache.remove(key)
            print(f"Deleted Key {key}")
        else:
            print("Invalid delete_key command")

    @staticmethod
    def invalid_command(cache: Cache[K, V], parts: list) -> None:
        print("Invalid command")
