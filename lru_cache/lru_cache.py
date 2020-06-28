from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.maxsize = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]

    def put(self, key: int, value: int) -> None:
        if len(self) == self.maxsize:
            if key in self:
                del self[key]
            else:
                lru_item = next(iter(self))
                del self[lru_item]
        self[key] = value
        self.move_to_end(key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
