from typing import TypeVar

T = TypeVar('T')

def get_item(list: list[t], index: int) -> T:
    return list[index]

list_int = get_item([1, 2, 3], 1)
list_stre = get_item(["a", "b", "c"], 1)