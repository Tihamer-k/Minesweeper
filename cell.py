from tkinter import Button


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

    @staticmethod
    def left_click_actions(event):
        print(event)
        print("soy el clic izquierdo")

    @staticmethod
    def right_click_actions(event):
        print(event)
        print("soy el clic derecho")

    @staticmethod
    def randomize_mines():
        pass
