import tkinter as tk
import time

class Canvas:
    def __init__(self, width=400, height=400, title="Canvas"):
        self._tk = tk.Tk()
        self._tk.title(title)
        self._canvas = tk.Canvas(self._tk, width=width, height=height)
        self._canvas.pack()
        self._mouse_x = 0
        self._mouse_y = 0
        self._last_click = (0, 0)
        self._canvas.bind("<Motion>", self._track_mouse)
        self._canvas.bind("<Button-1>", self._click)
        self._tk.update()

    def _track_mouse(self, event):
        self._mouse_x = event.x
        self._mouse_y = event.y

    def _click(self, event):
        self._last_click = (event.x, event.y)
        self._click_var.set(1)

    def get_mouse_x(self):
        return self._mouse_x

    def get_mouse_y(self):
        return self._mouse_y

    def get_last_click(self):
        return self._last_click

    def wait_for_click(self):
        self._click_var = tk.IntVar()
        self._tk.wait_variable(self._click_var)

    def create_rectangle(self, x1, y1, x2, y2, color="black"):
        return self._canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

    def set_color(self, obj_id, color):
        self._canvas.itemconfig(obj_id, fill=color, outline=color)

    def find_overlapping(self, x1, y1, x2, y2):
        return self._canvas.find_overlapping(x1, y1, x2, y2)

    def moveto(self, obj_id, x, y):
        coords = self._canvas.coords(obj_id)
        width = coords[2] - coords[0]
        height = coords[3] - coords[1]
        self._canvas.coords(obj_id, x, y, x + width, y + height)
        self._tk.update()

    def update(self):
        self._tk.update()

    def mainloop(self):
        self._tk.mainloop()

    def pause(self, ms):
        self._tk.after(ms)
        self._tk.update()
