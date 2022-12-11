from tkinter import Button


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None

    def create_btn_obj(self, location):
        btn = Button(
            location,
            text='Prueba'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        self.cell_btn_obj = btn

    def left_click_actions(self, event):
        print(event)
        print("Me diste clic")

