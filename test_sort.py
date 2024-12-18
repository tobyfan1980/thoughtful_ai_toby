import unittest

from sort_bot import SortBot, StackType

class TestUtils(unittest.TestCase):
    def test_standard(self):
        """
        test not bulky and not heavy
        :return:
        """
        print(f"Running test: {self.id()}")
        sort_bot = SortBot()
        self.assertEqual(sort_bot.sort(1,1,1,10), StackType.STANDARD)
        self.assertEqual(sort_bot.sort(10,10,10, 5), StackType.STANDARD)

    def test_special(self):
        """
        test either bulky or heavy
        :return:
        """
        print(f"Running test: {self.id()}")
        sort_bot = SortBot()
        self.assertEqual(sort_bot.sort(200, 100, 100, 10), StackType.SPECIAL)
        self.assertEqual(sort_bot.sort(10, 10, 10, 25), StackType.SPECIAL)

        # edge cases
        self.assertEqual(sort_bot.sort(100, 100, 100, 10), StackType.SPECIAL)
        self.assertEqual(sort_bot.sort(10, 100, 100, 20), StackType.SPECIAL)

    def test_reject(self):
        """
        test both bulky and heavy or illegal input
        :return:
        """
        print(f"Running test: {self.id()}")
        sort_bot = SortBot()
        self.assertEqual(sort_bot.sort(200, 100, 100, 30), StackType.REJECTED)
        self.assertEqual(sort_bot.sort(1000000, 10, 10, 25), StackType.REJECTED)

        # edge cases
        self.assertEqual(sort_bot.sort(100, 100, 100, 20), StackType.REJECTED)

    def test_illegal_input(self):
        """
        test illegal input as non-positive value
        :return:
        """
        print(f"Running test: {self.id()}")
        sort_bot = SortBot()
        with self.assertRaises(ValueError):
            sort_bot.sort(0, 100, 100, 30)
        with self.assertRaises(ValueError):
            sort_bot.sort(10, -10, 100, 30)
        with self.assertRaises(ValueError):
            sort_bot.sort(10, 100, -2, 30)
        with self.assertRaises(ValueError):
            sort_bot.sort(10, 100, 10, 0)


if __name__ == '__main__':
    unittest.main()


