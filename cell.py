import random
from tkinter import Button, Label
import settings as s


def get_cell_by_axis(x, y):
    # Return a cell object based on the value of x, y
    for cell in Cell.all:
        if cell.x == x and cell.y == y:
            return cell


class Cell:
    all = []
    cell_count = s.CELL_COUNT
    cell_count_label_obj = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
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

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg='black',
            fg='white',
            width=10,
            text=f"Total celdas:\n{Cell.cell_count}",
            font=("", 30)
        )
        Cell.cell_count_label_obj = label

    def left_click_actions(self, event):
        print(event)
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_length == 0:
                for cell_obj in self.surrounded_cells():
                    cell_obj.show_cell()
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
        if not self.is_opened:
            print(f"Hay {self.surrounded_cells_length} mina/s cerca")
            self.cell_btn_obj.configure(text=self.surrounded_cells_length)
            # Replace the text of cell count label
            Cell.cell_count -= 1
            if Cell.cell_count_label_obj:
                Cell.cell_count_label_obj.configure(
                    text=f"Total celdas:\n{Cell.cell_count}"
                )
        self.is_opened = True

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
