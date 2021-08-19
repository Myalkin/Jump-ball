import random
import time
from tkinter import *

from Ball import Ball

tk = Tk()
tk.title("JumpBall")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball_count = 10
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
    tk.update_idletasks()
    tk.update()
    time.sleep(0.001)
