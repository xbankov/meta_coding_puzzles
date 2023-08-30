from Warmup.ABCs import getSum


def test_ABCs():
    a, b, c = 1, 2, 3
    assert getSum(a, b, c) == 6


def test_ABCs2():
    a, b, c = 100, 100, 100
    assert getSum(a, b, c) == 300


def test_ABCs3():
    a, b, c = 85, 16, 93
    assert getSum(a, b, c) == 194
