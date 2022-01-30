class Node:
    def __init__(self, prev, next, key, value):
        self.prev = prev
        self.next = next
        self.value = value
        self.key = key


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # to maintain O 1 lookup, we'll store in a hash
        self.cache = {}

        # need to keep track of the key accesses in perhaps a seperate data
        # structure and when we reach capacity on the cache, eject based on the
        # item thats on top of the stack

        # we can use a doubly linked list to keep track of LRU/MRU, and then use
        # the dictionary to be able to retrieve whenever a get is done on the
        # item, so we can move it to the head of the list to indicate MRU. then
        # naturally the last item on the linked list will be the least recently
        # used and we can eject. it needs to be doubly linked because when we
        # use the dictionary to do the lookup, we need to cut ties forward and
        # backward and link those nodes to each other, and we want to be able to
        # do this without traversing the list to maintain O 1

        # create a linked list
        # create a dummy head
        # create a dummy tail
        self.head = Node(None, None, "head", "head")
        self.tail = Node(None, None, "tail", "tail")

        self.head.next = self.tail
        self.tail.prev = self.head

    def debug(self):
        print("cache contents")
        for k, v in self.cache.items():
            print(k, v.value)

        print("List from head")
        curr = self.head

        while curr:
            print(curr.value)
            curr = curr.next

        print("List from tail")
        curr = self.tail

        while curr:
            print(curr.value)
            curr = curr.prev

        print()

    def get_most_to_least(self):
        curr = self.head.next
        output = []

        while curr.value != "tail":
            output.append(curr.value)
            curr = curr.next

        return output

    def get(self, key: int) -> int:
        print("get", key)
        # return -1 if we dont see in the cache
        # check the dictionary to see if its a key we have
        if key not in self.cache:
            return -1

        # if so we need to find the node and move it to the most recently
        # accessed (head) of the linked list
        node = self.cache[key]

        self.remove(key)
        self.put(key, node.value)

        return node.value

    def remove(self, key):
        if key not in self.cache:
            return None

        node = self.cache[key]

        node.prev.next = node.next
        node.next.prev = node.prev

        del self.cache[key]

    def put(self, key: int, value: int) -> None:
        print("put", key)

        # always remove the key from the list to simplify logic
        self.remove(key)

        node = Node(self.head, self.head.next, key, value)
        self.head.next.prev = node
        self.head.next = node

        self.cache[key] = node

        # check capacity of the the cache and eject if we're over capacity
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            print("removing lru", lru.key)
            self.remove(lru.key)

        return None


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)class LRU
def test_1():
    cache = LRUCache(2)
    cache.put(1, 1)

    assert cache.get_most_to_least(), [1]

    cache.put(2, 2)
    assert cache.get_most_to_least(), [2, 1]

    cache.get(1)
    assert cache.get_most_to_least(), [1, 2]

    cache.put(3, 3)
    assert cache.get_most_to_least(), [3, 1]

    cache.get(2)
    assert cache.get_most_to_least(), [3, 1]

    cache.put(4, 4)
    assert cache.get_most_to_least(), [4, 3]

    cache.get(1)
    assert cache.get_most_to_least(), [4, 3]

    cache.get(3)
    assert cache.get_most_to_least(), [3, 4]

    cache.get(4)
    assert cache.get_most_to_least(), [4, 3]
