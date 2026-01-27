import unittest

from ex14 import check_fragment


class MyTestCase(unittest.TestCase):
    def test_check_fragment(self):
        input_ = [3, 1, 2, 1, 3, 1, 2, 1]
        r = check_fragment(4, input_)
        self.assertEqual(True, r)#dd assertion here

    def test_negative(self):
        input_ = [1, 2, 1, 2, 1, 2]
        r = check_fragment(3, input_)
        self.assertFalse(r)


if __name__ == '__main__':
    unittest.main()
