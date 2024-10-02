
class car:
    def __init__(self, w, h, s, x=0, y=0) -> None:
        self.w = w
        self.h = h 
        self.s = s 
        self.x = x
        self.y = y 

    def step(self, dt = 1):
        self.x += int(self.s * dt)

    def json(self):
        return { "w": self.w, "h": self.h, "x": self.x, "y": self.y }
    
    