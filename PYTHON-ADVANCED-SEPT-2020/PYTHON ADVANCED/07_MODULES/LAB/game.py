# main.py
#!/bin/env python3

import turtle
import time
import game


STAMP_SIZE = 20


game = game.Game()

screen = turtle.Screen()
screen.cv._rootwindow.resizable(False, False)
screen.title('Pong')
screen.bgcolor('#C6BDBC')
screen.setup(game.width, game.height)
screen.tracer(0)

ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.penup()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.shape('square')
paddle_a.color('#620B70')
paddle_a.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_a.penup()

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.shape('square')
paddle_b.color('#620B70')
paddle_b.shapesize(game.paddle_height / STAMP_SIZE, game.paddle_width / STAMP_SIZE)
paddle_b.penup()


# Text
text = turtle.Turtle()
text.penup()
text.color('white')
text.goto(0, game.height / 2 - 50)
text.write('Player A: 0, Player B: 0', align='center', font=('Courier', 20, 'normal'))
text.hideturtle()


# Listen to keyboard events
def player_a_up():
    game.paddle_a_up()


def player_a_down():
    game.paddle_a_down()


def player_b_up():
    game.paddle_b_up()


def player_b_down():
    game.paddle_b_down()


screen.listen()
screen.onkeypress(player_a_up, 'w')
screen.onkeypress(player_a_down, 's')
screen.onkeypress(player_b_up, 'Up')
screen.onkeypress(player_b_down, 'Down')


prev_points_a = None
prev_points_b = None
default_sleep = 0.005
sleep_time = default_sleep
index = 0

finished = turtle.Turtle()
finished.hideturtle()
already_finished = False


while True:
    game.tick()
    ball.goto(game.ball_pos())
    paddle_a.goto(game.paddle_a_pos)
    paddle_b.goto(game.paddle_b_pos)

    if prev_points_a != game.points_a or prev_points_b != game.points_b:
        text.clear()
        text.write(f'Player A: {game.points_a}, Player B: {game.points_b}', align='center', font=('Courier', 20, 'normal'))
        prev_points_a = game.points_a
        prev_points_b = game.points_b
        sleep_time = default_sleep

    if game.game_over and not already_finished:
        finished.clear()
        finished.write('Game Over', align='center', font=('Courier', 55, 'normal'))
        already_finished = True

    screen.update()
    time.sleep(sleep_time)

    if sleep_time > 0.0005 and index % 100 == 0:
        sleep_time -= 0.0005

    index += 1


# game.py
import random


class Game:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.__ball_pos = (0, 0)
        self.__ball_delta_x = 1
        self.__ball_delta_y = 1

        self.paddle_a_pos = (-self.width / 2 + 50, 0)
        self.paddle_b_pos = (self.width / 2 - 50, 0)

        self.paddle_height = self.height * 0.25
        self.paddle_width = 20

        self.points_a = 0
        self.points_b = 0

        self.game_over = False

    def tick(self):
        if self.points_a >= 5 or self.points_b >= 5:
            self.game_over = True
            return
        self.__perform_border_checking()
        self.__perform_paddle_hit_checking()
        x, y = self.__ball_pos
        self.__ball_pos = (x + self.__ball_delta_x, y + self.__ball_delta_y)

    def __perform_border_checking(self):
        x, y = self.__ball_pos
        if abs(y) >= (self.height / 2):
            self.__ball_delta_y *= -1

        if x <= -(self.width / 2):
            self.points_b += 1
            self.__ball_pos = (0, 0)
            self.__ball_delta_x *= random.choice([-1, 1])

        if x >= (self.width / 2):
            self.points_a += 1
            self.__ball_pos = (0, 0)
            self.__ball_delta_x *= random.choice([-1, 1])


    def __perform_paddle_hit_checking(self):
        x, y = self.__ball_pos

        a_x, a_y = self.paddle_a_pos
        hit_paddle_a = (a_x + self.paddle_width) == x and ((a_y - self.paddle_height / 2) <= y <= (a_y + self.paddle_height / 2))

        b_x, b_y = self.paddle_b_pos
        hit_paddle_b = (b_x - self.paddle_width) == x and ((b_y - self.paddle_height / 2) <= y <= (b_y + self.paddle_height / 2))

        if hit_paddle_a or hit_paddle_b:
            self.__ball_delta_x *= -1

    def ball_pos(self):
        return self.__ball_pos

    def paddle_a_up(self):
        x, y = self.paddle_a_pos
        if (y + 40) < (self.height / 2):
            self.paddle_a_pos = (x, y + 40)

    def paddle_a_down(self):
        x, y = self.paddle_a_pos
        if (y - 40) > -(self.height / 2):
            self.paddle_a_pos = (x, y - 40)

    def paddle_b_up(self):
        x, y = self.paddle_b_pos
        if (y + 40) < (self.height / 2):
            self.paddle_b_pos = (x, y + 40)

    def paddle_b_down(self):
        x, y = self.paddle_b_pos
        if (y - 40) > -(self.height / 2):
            self.paddle_b_pos = (x, y - 40)