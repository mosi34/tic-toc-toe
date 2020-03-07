import os
import itertools


class Game():
    def __init__(self):
        os.system('cls')
        self.cells = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.warning = '\n'
        self.quit = False
        self.player = ['X', 'O']
        self.turn = itertools.cycle(['X', 'O']).__next__

    def display(self):
        cells = self.cells
        print('  %s  |  %s  |  %s  ' % (cells[1], cells[2], cells[3]))
        print('-----------------')
        print('  %s  |  %s  |  %s  ' % (cells[4], cells[5], cells[6]))
        print('-----------------')
        print('  %s  |  %s  |  %s  ' % (cells[7], cells[8], cells[9]))
        print()

    def update_game(self, choose, player):
        self.warning = '\n'
        try:

            if self.cells[choose] != "X" and self.cells[choose] != 'O':
                self.cells[choose] = player
                self.refresh_screen()
            else:
                self.warning = 'You made mistake now is next Turn'
                self.refresh_screen()
        except IndexError:
            pass

    def print_header(self):
        print('Welcome to tic-toc-toe\n')
        if self.warning:
            print(self.warning)

    def refresh_screen(self):
        os.system('cls')
        self.print_header()
        self.display()

    def reset_game(self):
        ans = input('Do you want to play again ? (Y/N) > ').lower()
        if ans == 'y':
            self.cells = ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
            self.refresh_screen()
        self.exit()

    def is_winner(self, player):
        wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for win in wins:
            if self.cells[win[0]] == player and self.cells[win[1]] == player and self.cells[win[2]] == player:
                print(f'{player} wins !')
                return True
        return False

    def is_tie(self):
        if all(cell == 'X' or cell == 'O' for cell in self.cells):
            print('is tie!')
            return True

    def exit(self):
        self.quit = True


def main():

    board = Game()
    board.refresh_screen()

    while True:
        player = board.turn()
        x = int(input(f'{player} - choose 1-9 > '))
        board.update_game(x, player)

        if board.is_winner(player) or board.is_tie():
            board.reset_game()

        if board.quit:
            break


if __name__ == "__main__":
    main()
