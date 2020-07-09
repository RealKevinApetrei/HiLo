import random

class Score: # Scoring System
    def __init__(self, score=0): # Set Score
        self.score = score

    def add_score(self): # Add Score
        self.score += random.randint(1, 10)

    def remove_score(self): # Remove Score
        self.score -= random.randint(1, 10)

    def show_score(self):
        print(f"\n====================\nYour score is currently at (   {self.score}   )!\n====================\n")
