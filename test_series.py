from series import fibonacci, lucas, sum_series

# Fibonacci tests
# ****************************

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_six():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibonacci_thirteen():
    actual = fibonacci(13)
    expected = 233
    assert actual == expected

def test_fibonacci_seventeen():
    actual = fibonacci(17)
    expected = 1597
    assert actual == expected

#lucas tests

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_six():
    actual = lucas(6)
    expected = 18
    assert actual == expected

def test_lucas_seven():
    actual = lucas(7)
    expected = 29
    assert actual == expected

def test_lucas_thirteen():
    actual = lucas(13)
    expected = 521
    assert actual == expected

def test_lucas_seventeen():
    actual = lucas(17)
    expected = 3571
    assert actual == expected

# sum tests

def test_sum_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_two():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_three():
    actual = sum_series(3)
    expected = 2
    assert actual == expected

def test_sum_four():
    actual = sum_series(4)
    expected = 3
    assert actual == expected

def test_sum_five():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_six():
    actual = sum_series(6)
    expected = 8
    assert actual == expected

def test_sum_seven():
    actual = sum_series(7)
    expected = 13
    assert actual == expected
def test_sum_thirteen():
    actual = sum_series(13)
    expected = 233
    assert actual == expected

def test_sum_seventeen():
    actual = sum_series(17)
    expected = 1597
    assert actual == expected

def test_sum_lucas():
    actual = sum_series(9, 2, 1)
    expected = 76
    assert actual == expected

def test_sum_fibonacci():
    actual = sum_series(22, 0, 1)
    expected = 17711
    assert actual == expected

def nan_sum_series():
    actual = sum_series(1)
    expected = math.nan
    assert actual != expected

def sum_lucas():
    actual = sum_series(14)
    expected = 22
    assert actual == expected

def test_sum_series_fails():
    actual = sum_series('2', '3', 1)
    expected = 'This is neither a fibonacci nor a lucas series'
    assert actual == expected



