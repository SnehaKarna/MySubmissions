class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)    # LRU side
        self.right = Node(0, 0)   # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove node
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert at MRU
    def insert(self, node):
        prev = self.right.prev
        nxt = self.right

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key, value):

        # Key already exists
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Store in hashmap
        self.cache[key] = node

        # Put at MRU
        self.insert(node)

        # Capacity exceeded
        if len(self.cache) > self.capacity:

            # First real node = LRU
            lru = self.left.next

            self.remove(lru)

            # Remove from hashmap
            del self.cache[lru.key]