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
        ONE = 1
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        TWO = 2
        return dice.count(TWO) * TWO

# Pendiente refactorizar funcion threes a sixes

    @staticmethod
    def threes(*dice):
        number = dice.count(3)
        return number * 3

    @staticmethod
    def fours(*dice):
        number = dice.count(4)
        return number * 4

    @staticmethod
    def fives(*dice):
        number = dice.count(5)
        return number * 5

    @staticmethod
    def sixes(*dice):
        number = dice.count(6)
        return number * 6
    
    @staticmethod
    def score_pair(*dice):
        PAIR = 2
        for number in range(6, 0, -1):
            if dice.count(number) >= PAIR:
                return PAIR * number
        return 0

# Mejorable
    @staticmethod
    def two_pairs(*dice):
        PAIR = 2
        pairs = 0
        total = 0
        number = 1
        while pairs < 2 and number <= 6:
            if dice.count(number) >= 2:
                pairs += 1
                total += PAIR * number
            number += 1
        if pairs == 2:
            return total
        return 0

    @staticmethod
    def three_of_kind(*dice):
        THREE = 3
        for number in range(6, 0, -1):
            if dice.count(number) >= THREE:
                return THREE * number
        return 0
    
    @staticmethod
    def four_of_kind(*dice):
        FOUR = 4
        for number in range(6, 0, -1):
            if dice.count(number) >= FOUR:
                return FOUR * number
        return 0
    
    @staticmethod
    def small_straight(*dice):
        for number in range(1, 6):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)
    
    @staticmethod
    def large_straight(*dice):
        for number in range(2, 7):
            if dice.count(number) != 1:
                return 0
        return Yatzy.chance(*dice)

    @staticmethod
    def full_house(*dice):
        if Yatzy.down_pair(*dice) and Yatzy.three_of_kind(*dice):
            return Yatzy.down_pair(*dice) + Yatzy.three_of_kind(*dice)
        return 0
    
    @staticmethod
    def down_pair(*dice):
        PAIR = 2
        for number in range(6, 0, -1):
            if dice.count(number) == PAIR:
                return PAIR * number
        return 0
        
