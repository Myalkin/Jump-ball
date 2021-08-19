import random
import time
from tkinter import Tk, Canvas

from Ball import Ball
from Stick import Stick


class Game:
    def __init__(self, canvas_width, canvas_height, title, ball_count):
        self.is_exited = False
        self.game_started = True
        self.canvas = None
        self.tk = None
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.init_canvas(title)

        self.stick = None
        self.init_stick()

        self.balls = []
        self.init_balls(ball_count)

    def init_canvas(self, title):
        self.tk = Tk()
        self.tk.title(title)
        self.tk.resizable(0, 0)
        self.tk.wm_attributes("-topmost", 1)

        self.canvas = Canvas(self.tk, width=self.canvas_width, height=self.canvas_height, bd=0, highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas.bind_all('<Escape>', self.exit)

    def init_stick(self):
        self.stick = Stick(self.canvas, 'brown', stickX=self.canvas_width / 2, stickY=self.canvas_height / 5 * 4,
                           stickW=self.canvas_width / 10 * 3,
                           stickH=self.canvas_height / 100)

    def init_balls(self, ball_count):
        colors = ["red", "blue", "green", "orange", "yellow"]
        for i in range(ball_count):
            startX = random.randrange(1, 500)
            startY = random.randrange(1, 10)
            color = random.choice(colors)
            ball = Ball(self.canvas, self.stick, color, startX, startY)
            self.balls.append(ball)

    def exit(self, event):
        print("exit")
        self.is_exited = True

    def start(self):
        while not self.is_exited:
            if not self.game_started:
                self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2, text="You lose", fill='black',
                                        font='Helvetica 15 bold')
            else:
                for ball in self.balls:
                    ball.draw()
                    if ball.hit_bottom:
                        self.game_started = False
                self.stick.draw()

            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.01)
