class Node:
    def __init__(self, k, v, p):
        self.key = k
        self.value = v
        self.parent = p
        self.left = None
        self.right = None
        self.size = 1
        self.balance_factor = 0

    def get_by_key(self, key):
        if self.key == key:
            return Iterator(self)
        if key < self.key:
            return self.left.get_by_key(key) if self.left else Iterator(None)
        else:
            return self.right.get_by_key(key) if self.right else Iterator(None)

    def get_by_position(self, position):
        left_count = self.left.size if self.left else 0
        if left_count + 1 == position:
            return Iterator(self)
        if position <= left_count:
            return self.left.get_by_position(position)
        return self.right.get_by_position(position - left_count - 1)

    def insert(self, key, value):
        self.size += 1
        if key < self.key:
            if self.left:
                self.left = self.left.insert(key, value)
            else:
                self.left = Node(key, value, self)
        else:
            if self.right:
                self.right = self.right.insert(key, value)
            else:
                self.right = Node(key, value, self)
        return self

    def next(self):
        if self.right:
            tmp = self.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        tmp = self
        while tmp.parent and tmp == tmp.parent.right:
            tmp = tmp.parent
        return tmp.parent

class Iterator:
    def __init__(self, node):
        self.current_node = node
        self.previous_node = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_node:
            self.previous_node = self.current_node
            self.current_node = self.current_node.next()
            return self.previous_node
        raise StopIteration
