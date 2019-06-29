import unittest
import sys
from app import add_absolute, app


class TestMain(unittest.TestCase):
    def test_main(self):
        self.assertEqual(add_absolute(5), 6)
        self.assertEqual(add_absolute(-4), 5)

        with self.assertRaises(ValueError):
            add_absolute('123321')

    def test_app(self):
        with app.test_client() as c:
            r = c.get('/')
            self.assertEqual(r.status_code, 200)
