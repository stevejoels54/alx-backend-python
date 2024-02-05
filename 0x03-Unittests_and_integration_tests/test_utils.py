#!/usr/bin/env python3
"""utils unittests"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """Parameterize a unit test"""
    @parameterized.expand([
         ({"a": 1}, ["a"], 1),
         ({"a": {"b": 2}}, ["a"], {"b": 2}),
         ({"a": {"b": 2}}, ["a", "b"], 2),
     ])
    def test_access_nested_map(
           self,
           nested_map: Dict,
           path: Tuple[str],
           expected_result: Union[Dict, int]
           ) -> None:
        """ Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
