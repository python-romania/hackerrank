import random


class PaperRockScissors:

    accepted_values = ['r', 'p', 's']
    choice = ''
    cpu_choice_ = ''
    combinations = {
        'rp': 'p', 'rs': 'r',  'rr': 'draw',
        'pr': 'p', 'ps': 's',  'pp': 'draw',
        'sp': 's', 'sr': 'r',  'ss': 'draw',
    }

    def __init__(self):
        self.play_game()

    def cpu_choice(self):
        return random.choice(self.accepted_values)

    def play_game(self):
        self.choice = input('rock (r), paper (p) or scissors (s)? \nYour choice: ')
        if self.choice in self.accepted_values:
            print('Game has started, thinking....')
            self.cpu_choice_ = self.cpu_choice()
            if self.cpu_choice() == self.choice:
                self.replay_game(input('It\'s a draw, play again? (y/n) \nYour choice: '))
            else:
                if self.combinations[self.cpu_choice_ + self.choice] is self.cpu_choice_:
                    self.replay_game(input('So sorry, computer won, play again? (y/n) \n\nYour choice: '))
                else:
                    self.replay_game(input('Congratulations, you won, play again? (y/n) \n\nYour choice: '))
        else:
            self.replay_game(input('Value not accepted! Try again? (y/n) \nYour choice: '))

    def replay_game(self, replay):
        if replay in ['y', 'n']:
            if replay == 'y':
                self.play_game()
            else:
                print('Thank you for playing, have a nice day!')
        else:
            self.replay_game(input('Value not accepted! Try again? (y/n) \nYour choice: '))


game = PaperRockScrissors()
