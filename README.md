# square-root-calculator

A square root calculator using Python, pytest and Babylonian method.


## Requirements

- [Python3.12](https://www.python.org/downloads/);
- [poetry](https://python-poetry.org/docs/#installation) for running tests using pytest;


## Running

Call the main.py script along the square number.

Example with 10:
```bash
$ python src/square_root_calculator/main.py 10
result=3.162277660168379335963284232
```

Example with 16:
```bash
$ python src/square_root_calculator/main.py 16
result=4
```


## Testing (pytest)

```bash
$ poetry install
$ poetry shell
$ pytest
```

The output last line should be similar to this (number of current tests and time may vary):
```
========= 3 passed in 0.01s =========
```
