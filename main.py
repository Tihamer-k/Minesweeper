from tkinter import *
import settings as s
import utils as u

root = Tk()
# settings of the window
root.configure(bg="black")
root.title("Minesweeper (Buscaminas)")
root.geometry(f'{s.WIDTH}x{s.HEIGHT}')  # width x height
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="green",
    width=s.WIDTH,
    height=u.height_percentage(25)
)

left_frame = Frame(
    root,
    bg="yellow",
    width=u.width_percentage(25),
    height=u.height_percentage(75)
)
center_frame = Frame(
    root,
    bg="white",
    width=u.width_percentage(75),
    height=u.height_percentage(75)
)
top_frame.place(x=0, y=0)
left_frame.place(x=0, y=u.height_percentage(25))
center_frame.place(
    x=u.width_percentage(25),
    y=u.height_percentage(25)
)

# run the window
root.mainloop()
