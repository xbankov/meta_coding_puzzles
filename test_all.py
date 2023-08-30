from Level1.cafeteria import getMaxAdditionalDinersCount
from Level1.director_of_photography import getArtisticPhotographCount
from Level1.kaitenzushi import getMaximumEatenDishCount
from Level1.rotary_lock import getMinCodeEntryTime
from Level1.scoreboard_inference import getMinProblemCount
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


def test_kaitenzushi1():
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 1
    assert 5 == getMaximumEatenDishCount(N, D, K)


def test_kaitenzushi2():
    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 2
    assert 4 == getMaximumEatenDishCount(N, D, K)


def test_kaitenzushi3():
    N = 7
    D = [1, 2, 1, 2, 1, 2, 1]
    K = 2
    assert 2 == getMaximumEatenDishCount(N, D, K)


def test_rotary_lock1():
    N = 3
    M = 3
    C = [1, 2, 3]
    assert 2 == getMinCodeEntryTime(N, M, C)


def test_rotary_lock2():
    N = 10
    M = 4
    C = [9, 4, 4, 8]
    assert 11 == getMinCodeEntryTime(N, M, C)


def test_scoreboard_inference1():
    N = 6
    S = [1, 2, 3, 4, 5, 6]
    assert 4 == getMinProblemCount(N, S)


def test_scoreboard_inference2():
    N = 4
    S = [4, 3, 3, 4]
    assert 3 == getMinProblemCount(N, S)


def test_scoreboard_inference3():
    N = 4
    S = [2, 4, 6, 8]
    assert 4 == getMinProblemCount(N, S)
