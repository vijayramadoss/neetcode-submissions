class MyHashSet:

    def __init__(self):
        self.k=[]

    def add(self, key: int) -> None:
      if key not in self.k:
        self.k.append(key)

    def remove(self, key: int) -> None:
      if key in self.k:
        self.k.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.k


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)