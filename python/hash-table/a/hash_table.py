class HashTable:

    def __init__(self, size: int) -> None:
        self.size = size
        self.slots = [None] * self.size
        self.items = [None] * self.size

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, item):
        self.put(key, item)

    def get(self, key):
        hash = self.hash(key)
        item, stop, found, pos = None, False, False, hash
        while self.slots[pos] is not None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                item = self.items[pos]
            else:
                pos = self.rehash(pos)
                if pos == hash:
                    stop = True
        return item

    def put(self, key, value) -> None:
        hash = self.hash(key)

        if self.slots[hash] is None:
            self.slots[hash] = key
            self.items[hash] = value
        else:
            if self.slots[hash] == key:
                self.items[hash] = value
            else:
                rehash = self.rehash(hash)
                while self.slots[rehash] is not None and self.slots[rehash] != key:
                    rehash = self.rehash(rehash)
                if self.slots[rehash] is None:
                    self.slots[rehash] = key
                    self.items[rehash] = value
                else:
                    self.items[rehash] = value

    def hash(self, key: int) -> int:
        return key % self.size

    def rehash(self, key: int) -> int:
        return (key + 1) % self.size
