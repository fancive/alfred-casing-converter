import sys
import os
import unittest

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "alfred-casing-converter")
    )
)
from convert import camel_case_convert, snake_case_convert


class TestStringConverters(unittest.TestCase):
    def test_camel_case_convert(self):
        self.assertEqual(camel_case_convert("hello_world"), "helloWorld")
        self.assertEqual(camel_case_convert("this_is_a_test"), "thisIsATest")
        self.assertEqual(camel_case_convert("example"), "example")  # 无需转换
        # 测试camelCase输入，假设函数需要正确处理
        self.assertEqual(camel_case_convert("alreadyCamelCase"), "alreadyCamelCase")

    def test_snake_case_convert(self):
        self.assertEqual(snake_case_convert("HelloWorld"), "hello_world")
        self.assertEqual(snake_case_convert("ThisIsATest"), "this_is_a_test")
        self.assertEqual(snake_case_convert("example"), "example")  # 无需转换
        # 测试camelCase输入，假设函数需要正确处理
        self.assertEqual(snake_case_convert("alreadyCamelCase"), "already_camel_case")


if __name__ == "__main__":
    unittest.main()
