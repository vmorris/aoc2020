# My solutions for Advent of Code 2020

![Python package](https://github.com/vmorris/aoc2020/workflows/Python%20package/badge.svg)

## Setup

After cloning this repository, create a virtual environment, activate it, and install.
```
$ cd aoc2020
aoc2020 $ python3 -m venv venv
aoc2020 $ . venv/bin/activate
(venv) aoc2020 $ pip install -e .[test]
```

## Run daily solutions

eg.
```
(venv) aoc2020 $ python aoc2020/day03/solution.py 
153
2421944712
```

## Test Suite
Run the test suite with `pytest`
```
(venv) aoc2020 $ $ pytest --cov=aoc2020
============================ test session starts =============================
platform linux -- Python 3.8.6, pytest-6.1.2, py-1.9.0, pluggy-0.13.1
rootdir: /home/vmorris/git/github.com/vmorris/aoc2020
plugins: cov-2.10.1
collected 9 items                                                            

tests/test_day01.py ..                                                 [ 22%]
tests/test_day02.py ..                                                 [ 44%]
tests/test_day03.py ...                                                [ 77%]
tests/test_util.py ..                                                  [100%]

----------- coverage: platform linux, python 3.8.6-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
aoc2020/__init__.py             3      0   100%
aoc2020/day01/solution.py       8      0   100%
aoc2020/day02/solution.py      23      0   100%
aoc2020/day03/solution.py      24      0   100%
aoc2020/util.py                 5      0   100%
-----------------------------------------------
TOTAL                          63      0   100%


============================= 9 passed in 0.08s ==============================
```
