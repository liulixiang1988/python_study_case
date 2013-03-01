#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
from calculator import Calculator

class TddInPythonExample(unittest.TestCase):
    """Tdd In Python Example."""
    def setUp(self):
        self.cal = Calculator()

    def test_caculator_add_method_returns_correrct_result(self):
        result = self.cal.add(2, 2);
        self.assertEqual(4, result)

    def test_caculator_return_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.cal.add, "two", "three")

    def test_caculator_return_error_message_if_x_not_numbers(self):
        self.assertRaises(ValueError, self.cal.add, "two", 3)

    def test_caculator_return_error_message_if_y_not_numbers(self):
        self.assertRaises(ValueError, self.cal.add, 2, "three")