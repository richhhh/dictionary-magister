import unittest
import random
from avl import AVL

class AVLTester(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()
        #insert random permutation of [1, ..., 1000] list to avl tree
        ls = list(range(1, 1000))
        random.shuffle(ls)
        for v, k in enumerate(ls):
            self.avl.insert(k, v + 1)

    def test_is_all(self):
        test_set = set(range(1, 1000))
        #get value by key works fine
        all_values = {self.avl.get_value_by_key(x) for x in range(1, 1000)}
        self.assertSetEqual(all_values, test_set, "get_value_by_key fails")
        #get value by position works fine
        all_values = {self.avl.get_value_by_position(x) for x in range(1, 1000)}
        self.assertSetEqual(all_values, test_set, "get_value_by_position fails")
        #tree iterator works fine
        all_values = {x.value for x in self.avl}
        self.assertSetEqual(all_values, test_set, "tree iterator fails")

    def test_special_cases(self):
        self.assertIsNone(self.avl.get_value_by_key(-7))
        self.assertIsNone(self.avl.get_value_by_key(6666))
        self.assertIsNone(self.avl.get_value_by_position(6666))
        self.assertEqual(self.avl.get_value_by_position(-21), self.avl.get_value_by_position(1))


class AVLTester2(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()

    def test_some_things(self):
        self.avl.insert(277, 19)  # some random values choosen by me
        self.avl.insert(31, 14)  # order of inserted elements
        self.avl.insert(91, 99)  # forces rotation of nodes
        self.avl.insert(99, 22)
        self.avl.insert(111, 78)
        self.avl.insert(121, 91)
        self.assertListEqual([78, 91, 19], [x.value for x in self.avl.get_iterator_by_key(111)])
        self.assertListEqual([78, 91, 19], [x.value for x in self.avl.get_iterator_by_position(4)])

#suite1 = unittest.TestLoader().loadTestsFromTestCase(AVLTester)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(AVLTester2)
#all_tests = unittest.TestSuite([suite1, suite2])
#unittest.TextTestRunner(verbosity=2).run(all_tests)
unittest.main()
