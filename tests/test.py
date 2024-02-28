import sys
import os
import unittest

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "alfred-casing-converter")
    )
)
from convert import camel_case_convert, snake_case_convert, camel_to_snake_case


class TestStringConverters(unittest.TestCase):
    def test_camel_case_convert(self):
        self.assertEqual(camel_case_convert("hello_world"), "helloWorld")
        self.assertEqual(camel_case_convert("this_is_a_test"), "thisIsATest")
        self.assertEqual(camel_case_convert("example"), "example")
        self.assertEqual(camel_case_convert("alreadyCamelCase"), "alreadyCamelCase")
        self.assertEqual(
            camel_case_convert("Every moment of every day"), "everyMomentOfEveryDay"
        )

    def test_snake_case_convert(self):
        self.assertEqual(snake_case_convert("HelloWorld"), "hello_world")
        self.assertEqual(snake_case_convert("ThisIsATest"), "this_is_a_test")
        self.assertEqual(snake_case_convert("example"), "example")
        self.assertEqual(snake_case_convert("alreadyCamelCase"), "already_camel_case")
        self.assertEqual(snake_case_convert("already_snake_case"), "already_snake_case")
        self.assertEqual(
            snake_case_convert("Every moment of every day"), "every_moment_of_every_day"
        )

    def test_camel_to_snake_case(self):
        self.assertEqual(camel_to_snake_case("helloWorld"), "hello_world")


if __name__ == "__main__":
    unittest.main()
