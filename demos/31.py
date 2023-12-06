class LotterySystem:
    awards = {1: "Gold", 2: "Silver", 3: "Bronze"}

    def __init__(self):
        return

    @property
    def dealAward(self, rank):
        return self.awards[rank]

    @dealAward.setter
    def dealAward(self, rank, award):
        self.awards[rank] = award
