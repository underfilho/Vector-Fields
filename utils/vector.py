from utils.config import Config

def position(x, y):
    return Vector(x * Config.scale + Config.width/2, y * (-Config.scale) + Config.height/2)

def xy(x, y):
    return Vector((x - Config.width/2)/Config.scale, (y - Config.height/2)/(-Config.scale))

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def to_str(self):
        return str(self.x) + "x" + str(self.y)