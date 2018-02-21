from enum import Enum
import numpy as np


class CoinState(Enum):
    HEADS = 1
    TAILS = 0


class Game(object):
    def __init__(self, id):
        self._id = id
        self._rnd = np.random
        self._rnd.seed(self._id)

        self._status = CoinState.HEADS
        self._count_tails = 0
        self._count_win = 0
        #self._total_flips = 20
        self._flipNumber = 20
        self._fairCoin = 0.4

    def next_flip(self):
            fliplist = ""
            for i in range(0,self._flipNumber):
                fliplist = fliplist + str((np.random.binomial(1, self._fairCoin)))
            self._count_win = fliplist.count("001")

    def play(self):
        for i in range(1, self._flipNumber+1):
            self._rnd.sample()
            self._rnd.seed(self._id * self._flipNumber)
            self.next_flip()

    def get_reward(self):
        self.play()
        self._reward = -250 + (self._count_win * 100)
        return self._reward


myGame = Game(id=834)
print(myGame.get_reward())


class Cohort:
    def __init__(self, id, sim_number):
        self._id = id
        self._sim_number = sim_number
        self._players = []
        n = 1
        while n <= sim_number:
            player = Game(id*sim_number+n)
            self._players.append(player)
            n += 1

    def simulation(self):
        gameReward = []
        for player in self._players:
            gameReward.append(player.get_reward())
        return sum(gameReward) / len(gameReward)


trail1 = Cohort(id=412, sim_number=1000)

print(trail1.simulation())



