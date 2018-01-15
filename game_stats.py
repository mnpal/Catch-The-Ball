class GameStats():
    def __init__(self, catch_settings):
        self.catch_settings = catch_settings
        self.reset_stats()
        self.game_active = False

        file = open("highest_score.txt", "r")
        self.high_score = file.readline()
        file.close()
        if len(self.high_score) == 0:
            self.high_score = 0
        else:
            self.high_score = int(self.high_score)

    def reset_stats(self):
        self.ball_missed = self.catch_settings.ball_missing_limit
        self.score = 0
