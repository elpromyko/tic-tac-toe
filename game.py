import random


class TicTacToe(object):
    def __init__(self):
        self.winning_lines = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                         [[0, 0], (1, 0), (2, 0)],
                         [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)],
                         [(2, 0), (1, 1), (0, 2)]
                         ]
        self.current_score = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.player_move = True

    def show_score(self):
        print('  1 2 3\n'
              'A {a1} {a2} {a3}\n'
              'B {b1} {b2} {b3}\n'
              'C {c1} {c2} {c3}'.format(a1=self.current_score[0][0], a2=self.current_score[0][1],
                                        a3=self.current_score[0][2],
                                        b1=self.current_score[1][0], b2=self.current_score[1][1],
                                        b3=self.current_score[1][2],
                                        c1=self.current_score[2][0], c2=self.current_score[2][1],
                                        c3=self.current_score[2][2]))

    def make_a_move(self):
        if self.player_move:
            self.move = ''
            while self.move not in self.list_empty_spaces():
                try:
                    self.move = self.convert_to_index(input('Player moves to: '))
                except (IndexError, ValueError, TypeError, KeyError):
                    print('Type correct value, i.e. a1')
        else:
            self.cpu_move()

    def convert_to_index(self, user_input):
        d = {'a': 0, 'b': 1, 'c': 2}
        x = d[user_input[0]]
        y = int(user_input[1]) - 1
        return x, y

    def list_empty_spaces(self):
        empty_spaces = [(k, i) for k, m in enumerate(self.current_score) for i, j in enumerate(m) if ' ' in j]
        return empty_spaces

    def update_score(self):
        if self.player_move:
            self.current_score[self.move[0]][self.move[1]] = 'X'
        else:
            self.current_score[self.move[0]][self.move[1]] = 'O'

        self.player_move = not self.player_move  # switch between player and CPU

    def have_winner(self):
        if not self.list_empty_spaces():
            print('Draw')
            return True

        winning_lines_minus_e_fields = [[i for i in line if i not in self.list_empty_spaces()] for line in self.winning_lines]
        for line in winning_lines_minus_e_fields:
            if len(line) == 3:
                if self.current_score[line[0][0]][line[0][1]] == self.current_score[line[1][0]][line[1][1]] == \
                        self.current_score[line[2][0]][line[2][1]] == 'X':
                    print('Player wins')
                    return True

                elif self.current_score[line[0][0]][line[0][1]] == self.current_score[line[1][0]][line[1][1]] == \
                        self.current_score[line[2][0]][line[2][1]] == 'O':
                    print('CPU wins')
                    return True

        return False

    def cpu_move(self):
        #  check if there is two fields in winning line for CPU and put third 'O'
        o_fields = [(k, i) for k, m in enumerate(self.current_score) for i, j in enumerate(m) if 'O' in j]
        winning_lines_minus_o_fields = [[i for i in line if i not in o_fields] for line in self.winning_lines]
        for line in winning_lines_minus_o_fields:
            if len(line) == 1 and self.current_score[line[0][0]][line[0][1]] == ' ':
                self.move = line[0]
                return self.move

        #  check if there is two fields in winning line for player and put 'O' to block it
        x_fields = [(k, i) for k, m in enumerate(self.current_score) for i, j in enumerate(m) if 'X' in j]
        winning_lines_minus_x_fields = [[i for i in line if i not in x_fields] for line in self.winning_lines]
        for line in winning_lines_minus_x_fields:
            if len(line) == 1 and self.current_score[line[0][0]][line[0][1]] == ' ':
                self.move = line[0]
                return self.move

        self.move = random.choice(self.list_empty_spaces())
        return self.move


game = TicTacToe()  # create new instance of TicTacToe
game.show_score()  # render empty grid

# repeat until someone wins or a draw
while not game.have_winner():
    game.make_a_move()
    game.update_score()
    game.show_score()
