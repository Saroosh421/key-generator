"""test_cases.py"""
import unittest
import os
import sys
from key_generate.key_generator import generate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestGenerate(unittest.TestCase):
    (
        """
    Test cases for the generate function in the key_generator module.
    """
    )

    def test_default_values(self):
        (
            """
        Test with default values.
        """
        )
        key = generate().get_key()
        self.assertIsInstance(key, str)
        self.assertRegex(key, r"^[0-9a-fA-F]{3,10}(-[0-9a-fA-F]{3,10}){4}$")

    def test_mixed_case(self):
        (
            """
        Test with mixed case.
        """
        )
        key = generate(6, "-", 3, 6, "int", "mix", ["+", "*"]).get_key()
        self.assertIsInstance(key, str)
        self.assertRegex(key, r"^[0-9a-fA-F\+\*]{3,6}(-[0-9a-fA-F\+\*]{3,6}){5}$")

    def test_invalid_values(self):
        (
            """
        Test with invalid values.
        """
        )
        with self.assertRaises(ValueError):
            generate(type_of_value="invalid_value")
        with self.assertRaises(ValueError):
            generate(capital="invalid_value")


if __name__ == "__main__":
    unittest.main()
