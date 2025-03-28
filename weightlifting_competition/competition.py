class Competition():
    
    def __init__(self, competitors):
        self.competitors = competitors

    def winner(self):
        winner = self.competitors[0]
        for competitor in self.competitors:
            if competitor.sinclair() > winner.sinclair():
                winner = competitor
        return winner