import unittest

class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        return 10+ self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]


    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]

class TestBowlingGame(unittest.TestCase):
    
    def setUp(self):
        self.game =BowlingGame.BowlingGame()
    
    def testGutterGame(self):
        self.rollMany(0, 20)
        assert self.game.score() == 0
        
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score() == 300

    def testAllSpares(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)
