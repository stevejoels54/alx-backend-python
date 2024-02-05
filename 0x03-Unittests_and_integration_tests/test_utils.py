#!/usr/bin/env python3
"""utils unittests"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
           self,
           nested_map: Dict,
           path: Tuple[str],
           exception: Exception
           ) -> None:
        """ Test access nested map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mock HTTP calls"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
              self,
              test_url: str,
              test_payload: Dict
              ) -> None:
        """Tests get json function"""
        atts = {'json.return_value': test_payload'}
        with patch('requests.get', return_value=Mock(**atts)) as get_mthd:
            self.assertEqual(get_json(test_url), test_payload)
            get_mthd.assert_called_once_with(test_url)
