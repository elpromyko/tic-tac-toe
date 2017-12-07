import random


class ScoreTable(object):
    def __init__(self):
        # self.score_array = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        # self.score_array = [[' '] * 3 for i in range(3)]
        self.player_move = True
        self.current_score = {'a1': ' ', 'a2': ' ', 'a3': ' ',
                              'b1': ' ', 'b2': ' ', 'b3': ' ',
                              'c1': ' ', 'c2': ' ', 'c3': ' '
                              }

    def show_score(self):
        print('  1 2 3\n'
              'A {a1} {a2} {a3}\n'
              'B {b1} {b2} {b3}\n'
              'C {c1} {c2} {c3}'.format(a1=self.current_score['a1'], a2=self.current_score['a2'],
                                        a3=self.current_score['a3'],
                                        b1=self.current_score['b1'], b2=self.current_score['b2'],
                                        b3=self.current_score['b3'],
                                        c1=self.current_score['c1'], c2=self.current_score['c2'],
                                        c3=self.current_score['c3']))

    def who_moves(self):
        if self.player_move:
            print('Player\'s move')
        else:
            print('Cpu\'s move')

    def make_a_move(self):
        if self.player_move:
            self.move = input('You move to: ')
        else:
            self.move = random.choice(self.empty_spaces())
            print('CPU moves to {}'.format(self.move))
        self.player_move = not self.player_move  # switch between player and CPU
        return self.move, self.player_move

    def empty_spaces(self):
        empty_spaces = [key for key in self.current_score.keys() if self.current_score[key] == ' ']
        return empty_spaces

    def update_score(self):
        if self.player_move:
            self.current_score[self.move] = 'O'
        else:
            self.current_score[self.move] = 'X'

        self.rows_columns_diagonals = {
            '1': [self.current_score['a1'], self.current_score['b1'], self.current_score['c1']],  # \
            '2': [self.current_score['a2'], self.current_score['b2'], self.current_score['c2']],  # columns
            '3': [self.current_score['a3'], self.current_score['b3'], self.current_score['c3']],  # /
            'A': [self.current_score['a1'], self.current_score['a2'], self.current_score['a3']],  # \
            'B': [self.current_score['b1'], self.current_score['b2'], self.current_score['b3']],  # rows
            'C': [self.current_score['c1'], self.current_score['c2'], self.current_score['c3']],  # /
            'ul_dr': [self.current_score['a1'], self.current_score['b2'], self.current_score['c3']],  #
            'dl_ur': [self.current_score['c1'], self.current_score['b2'], self.current_score['a3']],  # diagonals
        }

    def have_winner(self):
        for list in self.rows_columns_diagonals.values():
            if list.count('X') == 3:
                print('Player X wins')
            if list.count('O') == 3:
                print('Player O wins')
        # if ' ' not in self.empty_spaces():  # wrong condition
        #     print('Draw')                    # needs to be fixed


new_sc_tb = ScoreTable()  # create new instance of ScoreTable

new_sc_tb.show_score()  # shows actual score

new_sc_tb.who_moves()  # who is moving now
new_sc_tb.make_a_move()
new_sc_tb.update_score()
new_sc_tb.have_winner()
new_sc_tb.show_score()
