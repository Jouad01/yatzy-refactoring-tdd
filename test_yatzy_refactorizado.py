import pytest
from yatzy_refactorizado import Yatzy

def test_chance():
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)

def test_yatzy():
    assert 50 == Yatzy.yatzy(1, 1, 1, 1, 1)
    assert 0 == Yatzy.yatzy(1, 1, 1, 2, 1)

def test_ones():
    assert 0 == Yatzy.ones(4, 4, 4, 4, 3)
    assert 5 == Yatzy.ones(1, 1, 1, 1, 1)

def test_twos():
    assert 0 == Yatzy.twos(1, 3, 4, 4, 5)
    assert 4 == Yatzy.twos(2, 3, 5, 4, 2)

# Pendiente refactorizar test threes a sixes

def test_threes():
    assert 9 == Yatzy.threes(3, 3, 3, 4, 5)
    assert 15 == Yatzy.threes(3, 3, 3, 3, 3)
    assert 0 == Yatzy.threes(1, 1, 1, 1, 1)

def test_fours():
    assert 20 == Yatzy.fours(4, 4, 4, 4, 4)
    assert 4 == Yatzy.fours(1, 2, 3, 4)
    assert 0 == Yatzy.fours(1, 2, 3, 5)

def test_fives():
    assert 25 == Yatzy.fives(5, 5, 5, 5, 5)
    assert 5 == Yatzy.fives(1, 2, 3, 4, 5)
    assert 0 == Yatzy.fives(1, 2, 3, 4, 6)

def test_sixes():
    assert 30 == Yatzy.sixes(6, 6, 6, 6, 6)
    assert 6 == Yatzy.sixes(1, 2, 3, 4, 6)
    assert 0 == Yatzy.sixes(1, 2, 3, 4, 5)

def test_score_pair():
    assert 8 == Yatzy.score_pair(3, 3, 3, 4, 4)
    assert 6 == Yatzy.score_pair(3, 3, 3, 3, 1)
    assert 0 == Yatzy.score_pair(1, 2, 3, 4, 5)

def test_two_pairs():
    assert 8 == Yatzy.two_pairs(1, 1, 2, 3, 3)
    assert 0 == Yatzy.two_pairs(1, 1, 2, 3, 4)
    assert 6 == Yatzy.two_pairs(1, 1, 2, 2, 2)
    assert 0 == Yatzy.two_pairs(1, 2, 3, 4, 5)

def test_three_of_kind():
    assert 9 == Yatzy.three_of_kind(3, 3, 3, 3, 1)
    assert 0 == Yatzy.three_of_kind(1, 2, 3, 4, 5)

def test_four_of_kind():
    assert 8 == Yatzy.four_of_kind(2, 2, 2, 2, 5)
    assert 0 == Yatzy.four_of_kind(2, 2, 2, 5, 5)

def test_small_straight():
    assert 15 == Yatzy.small_straight(1, 2, 3, 4, 5)
    assert 0 == Yatzy.small_straight(4, 2, 4, 2, 1)
    assert 0 == Yatzy.small_straight(3, 3, 1, 1, 2)
    assert 0 == Yatzy.small_straight(6, 6, 6, 6, 6)
    
def test_large_straight():
    assert 20 == Yatzy.large_straight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.large_straight(3, 1, 3, 1, 2)
    assert 0 == Yatzy.large_straight(6, 2, 2, 5, 6)
    assert 0 == Yatzy.large_straight(2, 1, 5, 4, 6)

def test_full_house():
    assert 8 == Yatzy.full_house(1, 1, 2, 2, 2)
    assert 0 == Yatzy.full_house(2, 4, 5, 6, 1)
    assert 0 == Yatzy.full_house(4, 4, 4, 4, 4)