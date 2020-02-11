from tkinter import *
from tkinter import ttk
from utils.config import Config
from utils.vector import *
from codes.field import Field
import math

class Plane:
    def __init__(self):
        self.__window = Tk()
        self.__canvas = None
        self.fX = ""
        self.fY = ""
        
        self.setup()
        self.__window.mainloop()

    def setup(self):
        self.__window.geometry('%ix%i' % (Config.width, Config.height))
        self.__window.resizable(False, False)
        self.__window.title(Config.name)
        self.__window.bind('<Return>', self.fill)

        self.__canvas = Canvas(self.__window, bg=Config.bgColor, highlightthickness=1, highlightbackground=Config.lineColor)
        self.__canvas.place(width=Config.width, height=Config.height)
        self.draw_axis()

        Label(self.__window, text="").place(x=10, y=8, width=150, height=23)
        Label(self.__window, text="F(x,y)=(").place(x=10, y=10, width=48, height=20)
        Label(self.__window, text=" )").place(x=120, y=10, height=20)

        self.eX = Entry(self.__window)
        self.eX.place(x=58, y=10, width=30)
        self.eY = Entry(self.__window)
        self.eY.place(x=90, y=10, width=30)
        

    def draw_axis(self):
        self.__canvas.create_line(0, Config.height/2, Config.width, Config.height/2, fill=Config.lineColor)
        self.__canvas.create_line(Config.width/2, 0, Config.width/2, Config.height, fill=Config.lineColor)

        nums = int(Config.height/Config.scale)
        for i in range(nums):
            self.__canvas.create_line(Config.width/2 - 2, i*Config.scale, Config.width/2 + 2, i*Config.scale, fill=Config.lineColor)
        nums = int(Config.width/Config.scale)
        for i in range(nums):
            self.__canvas.create_line(i*Config.scale, Config.height/2 - 2, i*Config.scale, Config.height/2 + 2, fill=Config.lineColor)

    def fill(self, event):
        self.fX = self.eX.get()
        self.fY = self.eY.get()

        if(self.fX != "" and self.fY != ""):
            self.__canvas.delete("all")
            self.draw_axis()
            Field.fill_field(self.__canvas, self.fX, self.fY)
    