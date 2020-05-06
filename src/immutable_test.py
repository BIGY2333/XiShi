import unittest
from hypothesis import given
import hypothesis.strategies as st
from immutable import *
class TestImmutableList(unittest.TestCase):
    def test_size(self):
        self.assertEqual(size(None), 0)
        self.assertEqual(size(['a']), 1)
        self.assertEqual(size(['a', 'b']), 2)
    def test_remove(self):
        self.assertEqual(remove(['a', 'b', 'c'], 0), ['b', 'c'])
        self.assertEqual(remove(['a', 'b', 'c'], 1), ['a', 'c'])
        self.assertEqual(remove(['a', 'b', 'c'], 2), ['a', 'b'])
    def test_add(self):
        self.assertEqual(add(['a', 'c'], 1, 'b'), ['a', 'b', 'c'])
        self.assertEqual(add(['a', 'c'], 2, 'b'), ['a', 'c', 'b'])
        self.assertEqual(add(['a', 'c'], 0, 'b'), ['b', 'a', 'c'])
    def test_from_list(self):
        test_data = [
            [],
            ['a'],
            ['a', 'b']
        ]
        for e in test_data:
            self.assertEqual((from_list(e)), e)
    def test_to_list(self):
        self.assertEqual(to_list(None), [])
        self.assertEqual(to_list(['a', None]), ['a'])
        self.assertEqual(to_list(['a', 'b', None]), ['a', 'b'])
    def test_find(self):
        self.assertEqual(find(None, 'a'), False)
        self.assertEqual(find(['a', 'b', 'c'], 'a'), 0)
        self.assertEqual(find(['a', 'b', 'c'], 'b'), 1)
    def test_filter(self):
        self.assertEqual(filter(['a', 1, 'c'], int), ['a', 'c'])
        self.assertEqual(filter(['a', 1, 'c'], str), [1])
    # def test_map(self):
    #     a = map(str)
    #     self.assertEqual(a, [])
    def test_reverse(self):
        self.assertEqual(reverse(['a', 'b']), ['b', 'a'])
        self.assertEqual(reverse(['a', 'b', 'c']), ['c', 'b', 'a'])
    def test_mconcat(self):
        self.assertEqual(mconcat(['a', 'b'], 'c'), ['a', 'b', 'c'])
        self.assertEqual(mconcat(['a', 'b'], ['c', 'd']), ['a', 'b', 'c', 'd'])
    @given(st.lists(st.integers()))
    def test_monoid_identity(self, lst):
        a = from_list(lst)
        self.assertEqual(mconcat([], a), a)
        self.assertEqual(mconcat(a, []), a)
    # def test_iter(self):
    #     x = [1, 2, 3]
    #
    #     # lst = from_list(x)
    #     # print(lst)
    #     tmp = []
    #     try:
    #         get_next = iterator(x)
    #         while True:
    #             tmp.append(get_next())
    #     except StopIteration:
    #         pass
    #     # self.assertEqual(x, tmp)
    #     self.assertEqual(to_list(x), tmp)
    #     get_next = iterator(None)
    #     self.assertRaises(StopIteration, lambda: get_next())