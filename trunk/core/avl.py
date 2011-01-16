from node import Node, Iterator

#~ class DummyIterator:
    #~ def __iter__(self):
        #~ return self
    #~ def __next__(self):
        #~ return StopIteration

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
        """Returns iterator representing first node with given key"""
        if self.root:
            return self.root.get_by_key(key)
        else:
            return Iterator(None)

    def get_iterator_by_position(self, n):
        """Returns iterator representing n-th key in whole tree

        If n is <= 0 it returns first element
        If n is greater than tree size then returns None"""
        if not self.root or n > self.root.size:
            return Iterator(None)
        if n <= 0:
            n = 1
        return self.root.get_by_position(n)

    def get_iterator_by_closest_match(self, key):
        """Same as get_iterator_by_key, but returns closest match if key's not found

        'Closest' means the previous one (or first element in a tree)
        For empty tree returns None exception"""
        pass

    ################################################################
    def get_value_by_key(self, key):
        """Returns value for a given key

        If tree doesn't contain key it returns None"""
        result = self.get_iterator_by_key(key)
        if result.current_node:
            return result.current_node.value
        return None

    def get_value_by_position(self, n):
        """Returns value for n-th key in the tree

        If n is <= 0 it returns first element
        If n is greater than tree size then returns None"""
        result = self.get_iterator_by_position(n)
        if result.current_node:
            return result.current_node.value
        return None

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
        return self.get_iterator_by_position(1)
