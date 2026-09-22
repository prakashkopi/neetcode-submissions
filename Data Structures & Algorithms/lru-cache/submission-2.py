class Node: 
    def __init__(self, key, value): 
        self.key, self.val= key, value
        self.next = self.prev = None

class LRUCache:
    # hashmap + dll for O(1) lookup and insert
    def __init__(self, capacity: int):
        self.cap= capacity
        self.cache= {}
    
        # create initial dll 
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev= self.right, self.left    

    # remove node from dll
    def remove(self, node):
        # L | (0,0) <--> (1,1) <--> (2,2) | R
        prev, nxt= node.prev, node.next
        prev.next, nxt.prev= nxt, prev
    
    # insert node to end of dll (right.next)
    def insert(self, node):
        # L | (0,0) <--> (1,1) <--> (2,2) | R
        prev, nxt= self.right.prev, self.right
        nxt.prev = prev.next = node
        node.next, node.prev= nxt, prev

    def get(self, key: int) -> int:
        # if key exists, remove and insert to the right, then return val
        if key in self.cache: 
            node= self.cache[key] # (0,0)
            self.remove(node)
            self.insert(node)
            return node.val # (0,0) --> we want the val so node.val
        return -1

    def put(self, key: int, value: int) -> None:
        # if key exists, remove before updating the value and insert at R
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])

        # if capacity has been reached, remove the LRU (at left pointer)
        # and delete from hashmap
        if len(self.cache) > self.cap: 
            lru= self.left.next
            lruKey= lru.key
            self.remove(lru)
            del self.cache[lruKey]

        
