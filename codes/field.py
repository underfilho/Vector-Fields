from tkinter import *
from utils.config import Config
from utils.vector import *
import math

class Field:
    def draw_point(x, y, canvas):
        vector = position(x, y)
        canvas.create_oval(vector.x-2, vector.y-2, vector.x+2, vector.y+2, fill='black')

    def draw_vector(x, y, angle, canvas):
        vector = position(x, y)
        xf = Config.scale * 0.5 * math.cos(angle)
        yf = Config.scale * -0.5 * math.sin(angle)
        
        canvas.create_line(vector.x - xf, vector.y - yf, vector.x + xf, vector.y + yf, fill=Config.lineColor, arrow=LAST)

    def fill_field(canvas, fX, fY):
        xt = int(Config.height/Config.scale/2)
        yt = int(Config.height/Config.scale/2)

        for x in range(-xt + 1, xt):
            for y in range(-yt + 1, yt):
                Field.draw_vector(x, y, math.atan2(Field.calculate_value(x, y, fY), Field.calculate_value(x, y, fX)), canvas)

    def calculate_value(x, y, func):
        return eval(func)

