

class out:
    def __init__(self, w, h, fill_char='-') -> None:
        self.buffer = []
        self.w  = w
        self.h = h 
        self.fill_char = fill_char
        self.__init_buffer()

    def __init_buffer(self):
        for _ in range(self.h):
            self.buffer.append([self.fill_char] * self.w) 

    def set_car(self, _car):
        w, h = _car.w, _car.h 
        x, y = _car.x, _car.y 
        self.fill_rect(x,y,w,h)
    
    def fill_rect(self, x, y, w, h, char='#' ):
        for yp in range(y, y+h):
            self.buffer[ yp ][ x:x+w ] = char * w 

    def print_buffer(self):
        for line in self.buffer:
            print("".join(line))

    def clear_car(self, _car):
        w, h = _car.w, _car.h 
        x, y = _car.x, _car.y

        self.fill_rect( x, y, w, h, char=self.fill_char )



    

    