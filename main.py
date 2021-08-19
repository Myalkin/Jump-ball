import random
import time
from tkinter import *

from Ball import Ball
from Stick import Stick

tk = Tk()
tk.title("JumpBall")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

stick = Stick(canvas, 'brown')
ball_count = 1
colors = ["red", "blue", "green", "orange", "yellow"]
balls = []
for i in range(ball_count):
    startX = random.randrange(1, 400)
    startY = random.randrange(1, 400)
    color = random.choice(colors)
    ball = Ball(canvas, color, startX, startY)
    balls.append(ball)

while True:
    for ball in balls:
        ball.draw()
    stick.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)
