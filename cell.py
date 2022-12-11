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
        self.cell_btn_obj = btn
