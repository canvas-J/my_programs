#!/usr/bin/env python3.5

from tkinter import *
from random import randint

class RandomBall(object):
    def __init__(self, canvas, screenwidth, screenheight):
        self.canvas = canvas
        self.xpos = randint(10, int(screenwidth))
        self.ypos = randint(10, int(screenheight))
        self.xspeed = randint(6, 12)
        self.yspeed = randint(6, 12)
        self.screenwidth = screenwidth
        self.screenheight = screenheight
        self.radius = randint(40, 70)
        color = lambda : randint(0, 255)
        self.color = '#%02x%02x%02x' % (color(), color(), color())

    def create_ball(self):
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        self.itm = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color,
                        outline=self.color)

    def move_ball(self):
        self.xpos += self.xspeed
        self.ypos += self.yspeed
        if self.ypos >= self.screenheight - self.radius:
            self.yspeed = -self.yspeed
        if self.ypos <= self.radius:
            self.yspeed = abs(self.yspeed)
        if self.xpos >= self.screenwidth - self.radius or self.xpos <= self.radius:
            self.xspeed = -self.xspeed
        self.canvas.move(self.itm, self.xspeed, self.yspeed)

class ScreenSaver:
    def __init__(self, num_balls):
        self.balls = []
        self.root = Tk()
        w, h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.attributes('-alpha', 0.3)
        self.root.bind('<Key>', self.myquit)
        self.root.bind('<Motion>', self.myquit)
        self.canvas = Canvas(self.root, width=w, height=h)
        self.canvas.pack()
        for i in range(num_balls):
            ball = RandomBall(self.canvas, screenwidth=w, screenheight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(50, self.run_screen_saver)

    def myquit(self, event):
        self.root.destroy()

if __name__ == "__main__":
    ScreenSaver(18)
