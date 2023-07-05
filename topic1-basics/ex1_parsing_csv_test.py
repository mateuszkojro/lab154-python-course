import unittest
from ex1_parsing_csv import parse_csv, parse_csv_type_checking

ASSET_DIR = "topic1-basics/assets/"

class TestParseCSV(unittest.TestCase):
    def test_parse_ex_sample1_easy(self):
        with open(ASSET_DIR + "ex1_sample1.csv", "r") as f:
            result = parse_csv(f.read())
            for key, value_array in result.items():
                for i, value in enumerate(value_array):
                    result[key][i] = str(value)
            self.assertEqual(result,
                {
                    "A": ["aa", "bb", "cc"],
                    "B": ["1", "2", "3"],
                    "C": ["1.1", "2.2", "3.3"],
                },
            )
    
    def test_parse_ex_sample1_full(self):
        with open(ASSET_DIR + "ex1_sample1.csv", "r") as f:
            result = parse_csv(f.read())
            self.assertEqual(result,
                {
                    "A": ["aa", "bb", "cc"],
                    "B": [1, 2, 3],
                    "C": [1.1, 2.2, 3.3],
                },
            )

    def test_parse_ex_sample2(self):
        with open(ASSET_DIR + "ex1_sample2.csv") as f:
            self.assertRaises(ValueError, parse_csv, f.read())

    def test_parse_ex_sample3(self):
        with open(ASSET_DIR + "ex1_sample3.csv") as f:
            self.assertEqual(
                parse_csv_type_checking(f.read()),
                {"A": ["aa", "1", "cc"], "B": [None, 2, 3], "C": [1.1, None, -3.3]},
            )


if __name__ == "__main__":
    unittest.main()
