# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:41:45 2018

@author: User
"""

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class RandomPlayer(Player):
    def move(self):
        import random
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        print("Pick your move:")
        pick = input()
        if pick in moves or pick == 'quit':
            return pick
        else:
            print("You made wrong choice!")
            self.move()


class ReflectPlayer(Player):
    def move(self):
        try:
            return self.their_move
        except AttributeError as their_move:
            import random
            return random.choice(moves)


class CyclePlayer(Player):
    def move(self):
        try:
            prev_pick = moves.index(self.my_move)
            if prev_pick == 2:
                return moves[0]
            else:
                return moves[prev_pick+1]
        except AttributeError as my_move:
            import random
            return random.choice(moves)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        self.move1 = self.p1.move()
        self.move2 = self.p2.move()
        if beats(self.move1, self.move2):
            self.score_p1 += 1
        elif beats(self.move2, self.move1):
            self.score_p2 += 1

        print(f"Player 1: {self.move1}  Player 2: {self.move2}")
        self.p1.learn(self.move1, self.move2)
        self.p2.learn(self.move2, self.move1)

    def play_game(self):
        print("Game start!")
        self.score_p1 = 0
        self.score_p2 = 0
        for round in range(1, 100):
            print(f"Round {round}:")
            self.play_round()
            if self.move1 == 'quit' or self.move2 == 'quit':
                print("Sorry, Player wants to quit the game")
                break
            if self.score_p1 == 3:
                print("Player1 win!")
                break
            elif self.score_p2 == 3:
                print("Player2 win!")
                break
            print(f"Score- Player1: {self.score_p1}, Player2: {self.score_p2}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
