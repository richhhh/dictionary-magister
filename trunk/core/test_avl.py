import unittest
import random
from avl import AVL


class AVLTester(unittest.TestCase):
    def setUp(self):
        self.avl = AVL()
        #insert random permutation of [1, ..., 1000) list to avl tree
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
        all_values = {value for key, value in self.avl}
        self.assertSetEqual(all_values, test_set, "tree iterator fails")

    def test_special_cases(self):
        self.assertIsNone(self.avl.get_value_by_key(-7))
        self.assertIsNone(self.avl.get_value_by_key(6666))
        self.assertIsNone(self.avl.get_value_by_position(6666))
        self.assertIsNone(self.avl.get_value_by_position(-21))
        self.assertIsNone(self.avl.get_value_by_closest_match(1001))
        self.assertEqual(self.avl.get_value_by_closest_match(-1), self.avl.get_value_by_key(1))
        self.assertIsNone(self.avl.get_value_by_closest_match(1001))
        self.assertEqual(self.avl.count(), 999)
        self.assertEqual(self.avl.count_subset(24, 124), 100)
        self.assertEqual(self.avl.count_subset(-10, 10), 9)
        self.assertEqual(self.avl.count_subset(999, 1001), 1)
        self.assertEqual(self.avl.count_subset(997, 1001), 3)
        self.assertEqual(self.avl.count_subset(1001, 1002), 0)
        self.assertIsNone(self.avl.get_closest_element_position(10001))

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
        self.assertListEqual([78, 91, 19], [value for key, value in self.avl.get_iterator_by_key(111)])
        self.assertListEqual([78, 91, 19], [value for key, value in self.avl.get_iterator_by_position(4)])
        self.assertEqual(self.avl.get_value_by_closest_match(71), 99)
        self.assertEqual(self.avl.get_value_by_closest_match(95), 22)
        self.assertEqual(self.avl.get_closest_element_position(21), 1)
        self.assertEqual(self.avl.get_closest_element_position(98), 3)
        self.avl.modify_by_key(111, 19)
        self.avl.modify_by_key(200, 21)
        self.assertEqual(self.avl.get_value_by_key(111), 19)
        self.avl.clear()
        self.assertIsNone(self.avl.get_value_by_closest_match(111))

#suite1 = unittest.TestLoader().loadTestsFromTestCase(AVLTester)
#suite2 = unittest.TestLoader().loadTestsFromTestCase(AVLTester2)
#all_tests = unittest.TestSuite([suite1, suite2])
#unittest.TextTestRunner(verbosity=2).run(all_tests)
unittest.main()
