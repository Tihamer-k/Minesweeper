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
            # text=f"{self.x},{self.y}"
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

    def surrounded_cells(self):
        cells = [
            get_cell_by_axis(self.x - 1, self.y - 1),
            get_cell_by_axis(self.x - 1, self.y),
            get_cell_by_axis(self.x - 1, self.y + 1),
            get_cell_by_axis(self.x, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y - 1),
            get_cell_by_axis(self.x + 1, self.y),
            get_cell_by_axis(self.x + 1, self.y + 1),
            get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_length(self):
        count = 0
        for cell in self.surrounded_cells():
            if cell.is_mine:
                count += 1
        return count

    def show_cell(self):
        print("Hay ", self.surrounded_cells_length, " mina/s por acá")
        self.cell_btn_obj.configure(text=self.surrounded_cells_length)

    def show_mine(self):
        print("¡Booooom!")
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
