class Highscore:

    def __init__(self, user_points):
        self.hs = open("high_scores", "r")
        self.high_score = self.hs.readline().strip()
        self.points = user_points
        self.high_score_set = False
        if self.high_score != "":
            self.high_score_set = True
        self.new_high_score = False

    def check_for_hs(self):
        if self.high_score == "":
            self.high_score = 0
            self.new_high_score = True
            self.high_score_set = True

        if self.high_score_set and self.points > int(self.high_score):
            self.new_high_score = True

        if self.new_high_score:
            hs = open("high_scores", "w")
            hs.write(str(self.points))

    def restart(self, user_points):
        self.hs = open("high_scores", "r")
        self.high_score = self.hs.readline().strip()
        self.points = user_points
        self.high_score_set = False
        if self.high_score != "":
            self.high_score_set = True
        self.new_high_score = False
