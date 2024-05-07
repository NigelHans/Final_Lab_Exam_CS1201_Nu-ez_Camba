import os
from utils.score import ScoreMixin
from utils.user_manager import UserManager
import random

class DiceGame(ScoreMixin):
    def __init__(self):
        self.data_folder = 'data'
        self.score_file = os.path.join(self.data_folder, 'scores.txt')
    def load_scores():
        pass
    def save_scores():
        pass
    def play_game(self):
        print("Welcome to Dice Game")
        print("1. Start Game")
        print("2. Top Scores")
        print("3. Logout")

        choice = int(input("Enter your Choice"))
        if choice == 1:
            CPU = 0
            self.username = 0

            while True:

                choice = input("Enter P to Play: ")
                if choice.upper == "P":
                    user_choice = random.randint(1,6)
                    CPU_choice = random.randint(1,6)

                    if CPU_choice < user_choice:
                        print("You Win")
                        self.points += 1
                    elif CPU_choice > user_choice:
                        CPU.points += 1
                        print("You Lose")
                    elif CPU_choice == user_choice:
                        print("It's a Tie")
        if choice == 2:
            return self.show_top_scores

        if choice == 3:
            return self.menu()


    def show_top_scores():
        pass
    def logout():
        pass
    def menu():
        print("Welcome to Dice Game")
        while True:
            try:
                print("1. Register")
                print("2. Login")
                print("3. Exit")

                choice = int(input("Enter your Choice"))
                if choice == 1:
                    pass
            except Exception:
                print("Error occurred.")
