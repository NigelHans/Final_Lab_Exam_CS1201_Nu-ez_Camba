import os
class ScoreMixin:
    def __init__(self, score_file):
        self.score_file = score_file
    
    def load_highest_scores(self):
        try:
            with open(self.score_file, 'r') as file:
                return int(file.read())
        except FileNotFoundError:
            return None
        except ValueError:
            print('Invalid Data.')
            return None
    
    def load_highest_score_date(self, score_file):
        try:
            with open(score_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return None


    