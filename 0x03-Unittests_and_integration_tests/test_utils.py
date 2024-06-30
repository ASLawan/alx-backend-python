#!/usr/bin/env python3
"""
    Module implementing test cases for access_nested_map
    function

"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b')),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Handles excpetions from test_access_map function"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


if __name__ == "__main__":
    unittest.main()
