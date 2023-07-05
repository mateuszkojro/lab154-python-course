import unittest
from ex1_parsing_csv import parse_csv


class TestParseCSV(unittest.TestCase):
    def test_parse_ex_sample1(self):
        with open("topic1-basics/assets/ex1_sample1.csv", "r") as f:
            self.assertEqual(
                parse_csv(f.read()),
                {
                    "A": ["aa", "bb", "cc"],
                    "B": [1, 2, 3],
                    "C": [1.1, 2.2, 3.3],
                },
            )

    # def test_parse_ex_sample2(self):
    #     with open("assets/ex1_sample2.csv") as f:
    #         self.assertEqual(
    #             parse_csv(f.read()),
    #             {"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9], "d": [10, 11, 12]},
    #         )


if __name__ == "__main__":
    unittest.main()
