# Ball Catcher
import tkinter as tk
import random

class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ball = self.canvas.create_oval(0, 0, 20, 20, fill='red')
        self.canvas.move(self.ball, random.randint(0, 380), random.randint(-500, 0))

    def move_down(self):
        self.canvas.move(self.ball, 0, 2)

class CatchGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=500, bg="light blue")
        self.canvas.pack()

        # creating basket
        self.basket = self.canvas.create_rectangle(0, 0, 60, 20, fill='blue')
        self.canvas.move(self.basket, 170, 470)
        self.master.bind('<Left>', self.move_left)
        self.master.bind('<Right>', self.move_right)
        self.basket_speed = 0

        # creating balls
        self.ball_objs = []
        for i in range(10):
            self.ball_objs.append(Ball(self.canvas))

        # creating score label
        self.score = 0
        self.score_label = tk.Label(self.master, text=f'Score: {self.score}')
        self.score_label.pack()

        # starting game loop
        self.game_loop()

    def game_loop(self):
        # move balls down
        for ball in self.ball_objs:
            ball.move_down()

        # check if any balls were caught
        for i in range(len(self.ball_objs)):
            ball_coords = self.canvas.coords(self.ball_objs[i].ball)
            if ball_coords[3] >= 470 and ball_coords[2] >= self.canvas.coords(self.basket)[0] and ball_coords[0] <= self.canvas.coords(self.basket)[2]:
                self.score += 1
                self.score_label.config(text=f'Score: {self.score}')
                self.canvas.delete(self.ball_objs[i].ball)
                self.ball_objs[i] = Ball(self.canvas)

        # move basket
        self.canvas.move(self.basket, self.basket_speed, 0)

        # wrap basket around screen
        basket_coords = self.canvas.coords(self.basket)
        if basket_coords[0] <= 0:
            self.basket_speed = 5
        elif basket_coords[2] >= 400:
            self.basket_speed = -5

        self.master.after(20, self.game_loop)

    def move_left(self, event):
        self.basket_speed = -5

    def move_right(self, event):
        self.basket_speed = 5

root = tk.Tk()
root.configure(background="green")
game = CatchGame(root)
root.mainloop()
