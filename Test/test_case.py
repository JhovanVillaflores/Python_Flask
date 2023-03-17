import unittest
from main_source import hello

class MyTestCase(unittest.TestCase):
    def test_print(self):
        self.assertEqual(1, hello.print_hi())

if __name__ == '__main__':
    unittest.main()