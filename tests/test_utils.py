import unittest
from utils import clean_command


class TestCleanCommand(unittest.TestCase):
    def test_lowercases_and_strips(self):
        self.assertEqual(clean_command("  Open BROWSER  "), "open browser")

    def test_already_clean_input(self):
        self.assertEqual(clean_command("hello friday"), "hello friday")


if __name__ == "__main__":
    unittest.main()
