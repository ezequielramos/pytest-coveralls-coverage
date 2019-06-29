import unittest
import sys

path = sys.path[0].split('/')
path.pop()

sys.path.append('/'.join(path))

from main import add_absolute

class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(add_absolute(5), 6)
        self.assertEqual(add_absolute(-4), 5)

        with self.assertRaises(ValueError):
            add_absolute('123321')
