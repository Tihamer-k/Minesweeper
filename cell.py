import random
from tkinter import Button
import settings as s


def get_cell_by_axis(x, y):
    # Return a cell object based on the value of x, y
    for cell in Cell.all:
        if cell.x == x and cell.y == y:
            return cell


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
        else:
            self.show_cell()

    def show_cell(self):
        # print(self.get_cell_by_axis(0,0))
        surrounded_cells = [
            get_cell_by_axis(self.x - 1, self.y - 1),
            get_cell_by_axis(self.x - 1, self.y),
            get_cell_by_axis(self.x - 1, self.y + 1),
            get_cell_by_axis(self.x, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y),
            get_cell_by_axis(self.x + 1, self.y + 1),
            get_cell_by_axis(self.x, self.y + 1)
        ]

        surrounded_cells = [cell for cell in surrounded_cells if cell is not None]
        print(surrounded_cells)

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
