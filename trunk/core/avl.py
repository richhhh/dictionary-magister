class AVL:
    """Implementation of AVL tree with some additional features
    
    Additional features:
    -is able to find n-th element
    -finding 'closest' match
    -finding next element
    """
    ################################################################
    def __init__(self):
        self.root = None
        
    ################################################################
    def insert(self, key, value):
        if self.root:
            self.root = self.root.insert(key, value)
        else:
            self.root = Node(key, value, None)

    ################################################################
    def get_iterator_by_key(self, key):
        """Returns iterator representing first node with given key
        
        If tree doesn't contain key it returns None exception"""
        if self.root:
            return self.root.get_by_key(key)
        else:
            return None
            
    def get_iterator_by_position(self, n):
        """Returns iterator representing n-th key in whole tree
        
        If n is <= 0 it returns first element
        If n is greater than tree size then returns None"""
        pass
        
    def get_iterator_by_closest_match(self, key):
        """Same as get_iterator_by_key, but returns closest match if key's not found
        
        'Closest' means the previous one (or first element in a tree)
        For empty tree returns None exception"""
        pass
        
    ################################################################
    def get_value_by_key(self, key):
        """Returns value for a given key
        
        If tree doesn't contain key it returns None"""
        return self.get_iterator_by_key(key).value
            
    def get_value_by_position(self, n):
        """Returns value for n-th key in the tree
        
        If n is <= 0 it returns first element
        If n is greater than tree size then returns None"""
        pass
    def get_value_by_closest_match(self, key):
        """Same as get_value_by_key, but returns closest match if key's not found
        
        'Closest' means the previous one (or first element in a tree)
        For empty tree returns None"""
        pass
        
    ################################################################        
    def count(self):
        """Size of the tree"""
        if self.root:
            return self.root.size
        else:
            return 0
    def count(self, begin, end):
        """Return number of elements with key in [begin, end)"""
        pass

    ################################################################
    def remove_by_key(self, key):
        """Remove node with a given key
        
        If key's not found it does nothing"""
        pass
    def remove_by_iterator(self, iterator):
        """Removes node which is represented by iterator"""
        pass

    ################################################################
    def __iter__(self):
        pass

class Node:
    def __init__(self, k, v, p):
        self.parent = p
        self.left = None
        self.right = None
        self.size = 1
        self.balance_factor = 0
        self.key = k
        self.value = v
    
    def get_by_key(self, key):
        if self.key == key:
            return self
        if key < self.key:
            if self.left:
                return self.left.get_by_key(key)
            else:
                return None
        else:
            if self.right:
                return self.right.get_by_key(key)
            else:
                return None
    
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
        
    def __iter__(self):
        return self
    def __next__(self):
        pass
