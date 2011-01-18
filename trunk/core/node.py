class Node:
    def __init__(self, k, v, p):
        self.key = k
        self.value = v
        self.parent = p
        self.left = None
        self.right = None
        self.size = 1
        self.height = 1

    def get_by_key(self, key):
        if self.key == key:
            return Iterator(self)
        if key < self.key:
            return self.left.get_by_key(key) if self.left else Iterator(self)
        else:
            return self.right.get_by_key(key) if self.right else Iterator(self.next())

    def get_by_position(self, position):
        left_count = self.left.size if self.left else 0
        if left_count + 1 == position:
            return Iterator(self)
        if position <= left_count:
            return self.left.get_by_position(position)
        return self.right.get_by_position(position - left_count - 1)

    def insert(self, key, value):
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
        if(self.calculate_balance() == -2):
            if self.right and self.right.calculate_balance() > 0:
                self.right = self.right.rotate_right()
            return self.rotate_left()
        if(self.calculate_balance() == 2):
            if self.left and self.left.calculate_balance() < 0:
                self.left = self.left.rotate_left()
            return self.rotate_right()
        self.update_data()
        return self

    def calculate_balance(self):
        left_height = self.left.height if self.left else 0
        right_height = self.right.height if self.right else 0
        return left_height - right_height

    def update_data(self):
        left_height = left_size = right_size = right_height = 0
        if self.left:
            left_height = self.left.height
            left_size = self.left.size
        if self.right:
            right_height = self.right.height
            right_size = self.right.size
        self.size = left_size + right_size + 1
        self.height = 1 + max(left_height, right_height)

    def rotate_right(self):
        new_root = self.left
        self.left = new_root.right
        new_root.right = self
        new_root.parent = self.parent
        self.parent = new_root
        if self.left:
            self.left.parent = self
        new_root.size = self.size
        self.update_data()
        new_root.update_data()
        return new_root
        
    def rotate_left(self):
        new_root = self.right
        self.right = new_root.left
        new_root.left = self
        new_root.parent = self.parent
        self.parent = new_root
        if self.right:
            self.right.parent = self
        self.update_data()
        new_root.update_data()
        return new_root

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
            return (self.previous_node.key, self.previous_node.value)
        raise StopIteration

    def get_key(self):
        return self.current_node.key if self.current_node else None

    def get_value(self):
        return self.current_node.value if self.current_node else None
