#!/usr/bin/env python3
"""Test module for the util functions"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for unittesting.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Testing nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
    ({}, ("a",), "'a'"),
    ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception_message):
        """
        Testing map exception
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertIn(expected_exception_message, str(context.exception))


class TestMemoize(unittest.TestCase):
    """
    Memoize testing class.
    """

    class TestClass:
        """
        Memoize test class
        """

        def a_method(self):
            """
            A method.
            """
            return 42

        @memoize
        def a_property(self):
            """
            memoize decorator.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Using memoize to test
        """
        with patch.object(self.TestClass, 'a_method',
                          return_value=42) as mock_method:
            instance = self.TestClass()
            result1 = instance.a_property()
            result2 = instance.a_property()
            mock_method.assert_called_once_with(instance)
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()
