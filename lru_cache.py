# class Node:: This line defines a class named Node. In Python, classes are blueprints for creating objects.
class Node:
    """
    def __init__(self, key, val):: This is a special method in Python classes called the constructor method. 
    It is automatically called when a new object of the class is created. 
    self is a reference to the instance of the class (the object being created). 
    key and val are parameters that will be used to initialize the object with a key and a value.
    """
    def __init__(self, key, val):
        # self.key, self.val = key, val: 
        # This line initializes two attributes of the 
        # object (self) - key and val - with the values passed to the constructor.

        self.key, self.val = key, val

        # self.prev = self.next = None: This line initializes two more attributes - prev and next - with the value None. 
        # These attributes are likely used in the context of linked lists to point to the previous and next nodes respectively.

        self.prev = self.next = None

class LRUCache:
    # automatically initialize LRUCache with capacity
    def __init__(self, capacity: int):
        # set cap to capacity
        self.cap = capacity
        # initialize hashmap using cache = {}
        self.cache = {}

        # dummy nodes
        # left = least recently used
        # right = most recently used
        self.left, self.right = Node(0, 0), Node(0, 0)

        # then att next and prev attributes to left and right
        # left.next is equals to right
        # right.prev is equals to left
        self.left.next, self.right.prev = self.right, self.left

    # helper function remove
    def remove(self, node):
        # 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        # if key is in the hashmap
        if key in self.cache:
            # reorder the linked list
            # 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        # if key is in the hashmap
        if key in self.cache:
            # remove the existing key and value in the hashmap
            self.remove(self.cache[key])
        # now insert the key and value in the hashmap
        # using self.cache[key] pointing to the Node(key, value)
        self.cache[key] = Node(key, value)
        
        # and then insert this key to the linked list using the hashmap
        self.insert(self.cache[key])

        # now check if the cache is greater than the capacity
        if len(self.cache) > self.cap:

            # now initialize lru to the least used node.
            # which is left.next
            lru = self.left.next
            
            # then use self.remove helper function to unlinked the node the least used node
            self.remove(lru)

            # then delete this node in the hashmap
            del self.cache[lru.key]


input = ["LRUCache","put","put","get","put","get","put","get","get","get"]
output = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# cache that store values
# store values using int as key and in as value. 
# 