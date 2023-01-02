import random
from tkinter import Button
import settings as s


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_obj(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_obj = btn

    def left_click_actions(self, event):
        print(event)
        if self.is_mine:
            self.show_mine()

    def show_mine(self):
        self.cell_btn_obj.configure(bg="red")

    @staticmethod
    def right_click_actions(event):
        print(event)
        print("soy el clic derecho")

    @staticmethod
    def randomize_mines():
        random_cells = random.sample(
            Cell.all, s.MINES_COUNT
        )
        print(random_cells)
        for random_cell in random_cells:
            random_cell.is_mine = True

    def __repr__(self):
        return f"Celda({self.x}, {self.y})"
