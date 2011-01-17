from node import Node, Iterator


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
        result = self.get_iterator_by_closest_match(key)
        return result if result.get_key() == key else Iterator(None)

    def get_iterator_by_position(self, n):
        """Returns iterator representing n-th key in whole tree

        If n >= tree size or n <= 0 then returns None"""
        if n <= 0 or n > self.count():
            return Iterator(None)
        return self.root.get_by_position(n)

    def get_iterator_by_closest_match(self, key):
        """Same as get_iterator_by_key, but returns closest match if key's not found

        'Closest' means the previous one (or first element in a tree)
        For empty tree returns None exception"""
        if self.root:
            return self.root.get_by_key(key)
        return Iterator(None)

    ################################################################
    def get_value_by_key(self, key):
        """Returns value for a given key

        If tree doesn't contain key it returns None"""
        return self.get_iterator_by_key(key).get_value()

    def get_value_by_position(self, n):
        """Returns value for n-th key in the tree

        If n is <= 0 it returns first element
        If n is greater than tree size then returns None"""
        return self.get_iterator_by_position(n).get_value()

    def get_value_by_closest_match(self, key):
        """Same as get_value_by_key, but returns closest match if key's not found

        'Closest' means the previous one (or first element in a tree)
        For empty tree returns None"""
        return self.get_iterator_by_closest_match(key).get_value()

    ################################################################
    def modify_by_iterator(self, iterator, new_value):
        if iterator.current_node:
            iterator.current_node.value = new_value

    def modify_by_key(self, key, new_value):
        self.modify_by_iterator(self.get_iterator_by_key(key), new_value)
    ################################################################
    def count(self):
        """Size of the tree"""
        if self.root:
            return self.root.size
        return 0

    def get_closest_element_position(self, key):
        element = self.get_iterator_by_closest_match(key).current_node
        if not element:
            return None
        result = 1 + element.left.size if element.left else 1
        while element.parent:
            if element.parent.right == element:
                result += element.parent.size - element.size
            element = element.parent
        return result

    def count_subset(self, begin, end):
        """Return number of elements with key in [begin, end)"""
        left = self.get_closest_element_position(begin)
        if not left:
            return 0
        right = self.get_closest_element_position(end)
        return right - left if right else self.count() - left + 1

    ################################################################
    def remove_by_key(self, key):
        """Remove node with a given key

        If key's not found it does nothing"""
        pass

    def remove_by_iterator(self, iterator):
        """Removes node which is represented by iterator"""
        pass

    def clear(self):
        self.root = None
    ################################################################
    def __iter__(self):
        return self.get_iterator_by_position(1)

