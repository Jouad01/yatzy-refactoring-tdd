from turtle import st
from pips import Pips


class Yatzy:

    def __init__(self, *dice):
        self.dice = list(dice)

    @staticmethod
    def chance(*dice):
        return sum(dice)

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) != 5:
            return 0
        return 50

    @staticmethod
    def ones(*dice):
        ONE = Pips.ONE.value
        return dice.count(1) * 1

    @staticmethod
    def twos(*dice):
        TWO = Pips.TWO.value
        return dice.count(2) * 2

# Pendiente refactorizar funcion threes a sixes - Finalizado

    @staticmethod
    def threes(*dice):
        THREE = Pips.THREE.value
        number = dice.count(3)
        return number * 3

    @staticmethod
    def fours(*dice):
        FOUR = Pips.FOUR.value
        number = dice.count(4)
        return number * 4

    @staticmethod
    def fives(*dice):
        FIVE = Pips.FIVE.value
        number = dice.count(5)
        return number * 5

    @staticmethod
    def sixes(*dice):
        SIX = Pips.SIX.value
        number = dice.count(6)
        return number * 6

    @staticmethod
    def score_pair(*dice):
        PAIR = 2
        for pip in Pips.reversedRange():
            if dice.count(pip) >= PAIR:
                return PAIR * pip
        return 0

# Fino
    
    @classmethod
    def two_pairs(cls, *dice):
        PAIR = 2
        pips_pairs = cls._pips_repeated(dice, PAIR)
        return sum(pips_pairs) * PAIR if len(pips_pairs) == 2 else 0

    @classmethod
    def three_of_kind(cls, *dice):
        THREE = 3
        pip = cls._big_pip_repeated(dice, THREE)
        return pip * THREE if pip else 0

    @classmethod
    def four_of_kind(cls, *dice):
        FOUR = 4
        pip = cls._big_pip_repeated(dice, FOUR)
        return pip * FOUR if pip else 0

    @classmethod
    def _big_pip_repeated(cls, dice, times):
        pips = cls._pips_repeated(dice, times)
        return pips[0] if pips else []

    @classmethod
    def _pips_repeated(cls, dice, times):
        return list(filter(lambda pip: dice.count(pip) >= times, Pips.reversedRange()))

    @classmethod
    def small_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.SIX) - set(dice) else 0

    @classmethod
    def large_straight(cls, *dice):
        return cls.chance(*dice) if not Pips.minus(Pips.ONE) - set(dice) else 0

    @classmethod
    def full_house(cls, *dice):
        if cls.down_pair(*dice) and cls.three_of_kind(*dice):
            return cls.down_pair(*dice) + cls.three_of_kind(*dice)
        return 0

    @classmethod
    def down_pair(cls, *dice):
        PAIR = 2
        for pip in Pips.reversedRange():
            if dice.count(pip) == PAIR:
                return PAIR * pip
        return 0
