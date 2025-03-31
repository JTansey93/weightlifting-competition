class Competition():
    
    def __init__(self, competitors):
        self.competitors = competitors
        self.current_lift = "Snatch"

    def next_lifter(self):
        if self.current_lift == "Snatch":
            min_lift = self.competitors[0].next_snatch
            next_lifter = self.competitors[0]
            for competitor in self.competitors:
                if competitor.next_snatch < min_lift:
                    min_lift = competitor.next_snatch
                    next_lifter = competitor
            return next_lifter
        else:
            min_lift = self.competitors[0].next_cnj
            next_lifter = self.competitors[0]
            for competitor in self.competitors:
                if competitor.next_cnj < min_lift:
                    min_lift = competitor.next_cnj
                    next_lifter = competitor
            return next_lifter


    def winner(self):
        winner = self.competitors[0]
        for competitor in self.competitors:
            if competitor.sinclair() > winner.sinclair():
                winner = competitor
        return winner