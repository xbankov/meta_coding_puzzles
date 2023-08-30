from Level1.cafeteria import getMaxAdditionalDinersCount
from Level1.director_of_photography import getArtisticPhotographCount
from Warmup.ABCs import getSum
from Warmup.AllWrong import getWrongAnswers
from Warmup.battleship import getHitProbability


def test_ABCs1():
    a, b, c = 1, 2, 3
    assert getSum(a, b, c) == 6


def test_ABCs2():
    a, b, c = 100, 100, 100
    assert getSum(a, b, c) == 300


def test_ABCs3():
    a, b, c = 85, 16, 93
    assert getSum(a, b, c) == 194


def test_allwrong1():
    N, C = 3, "ABA"
    assert "BAB" == getWrongAnswers(N, C)


def test_allwrong2():
    N, C = 5, "BBBBB"
    assert "AAAAA" == getWrongAnswers(N, C)


def test_battleship1():
    R = 2
    C = 3
    G = [[0, 0, 1], [1, 0, 1]]
    assert 0.50000000 == getHitProbability(R, C, G)


def test_battleship2():
    R = 2
    C = 2
    G = [[1, 1], [1, 1]]
    assert 1.00000000 == getHitProbability(R, C, G)


def test_cafeteria1():
    N = 10
    K = 1
    M = 2
    S = [2, 6]
    assert 3 == getMaxAdditionalDinersCount(N, K, M, S)


def test_cafeteria2():
    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]
    assert 1 == getMaxAdditionalDinersCount(N, K, M, S)


def test_director_of_photography1():
    N = 5
    C = "APABA"
    X = 1
    Y = 2
    assert 1 == getArtisticPhotographCount(N, C, X, Y)


def test_director_of_photography2():
    N = 5
    C = "APABA"
    X = 2
    Y = 3
    assert 0 == getArtisticPhotographCount(N, C, X, Y)


def test_director_of_photography3():
    N = 8
    C = ".PBAAP.B"
    X = 1
    Y = 3
    assert 3 == getArtisticPhotographCount(N, C, X, Y)
