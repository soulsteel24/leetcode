class MyHashMap:

    def __init__(self):
        MAX_ARR=10**6+1
        self.arr_map=[-1]*(MAX_ARR)

    def put(self, key: int, value: int) -> None:
        self.arr_map[key]=value

    def get(self, key: int) -> int:
        return self.arr_map[key]

    def remove(self, key: int) -> None:
        self.arr_map[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)