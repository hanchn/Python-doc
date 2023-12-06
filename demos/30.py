class award:
    awards = {1: "Gold", 2: "Silver", 3: "Bronze"}

    def __init__(self):
        return

    def get_award(self, rank):
        return award.awards[rank]

    def set_awards(self, award_number, award):
        self.awards[award_number] = award
