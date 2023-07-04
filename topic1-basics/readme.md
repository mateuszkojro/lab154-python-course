# Topic 1 Basics

## Exercise 1

Write a function that can parse data in the CSV format:

```
A,B,C
aa,1,1.1
bb,2,2.2
cc,3,3.3
```

implemented function should take a string as an input eg:

```python
content = "A,B,C\naa,1,1.1\nbb,2,2.2\ncc,3,3.3"
```

and output:

```python
{
    "A": ["aa", 1, 1.1],
    "B": ["bb", 2, 2.2],
    "C": ["cc", 3, 3.3],
}
```

To check your code implement function `parse_csv` in `topic1-basics/ex1_parsing_csv.py` and run:

```bash
python topic1-basics/ex1_parsing_csv_test.py
```

Example data in `topic1-basics/assets/ex1_sample1.csv` and `topic1-basics/assets/ex1_sample2.csv`

Some sources:

[1] Python official documentation on working with strings: <https://docs.python.org/3/library/stdtypes.html#textseq>

[2] Python String Methods in maybe a bit simpler way: <https://www.geeksforgeeks.org/python-string-methods/>