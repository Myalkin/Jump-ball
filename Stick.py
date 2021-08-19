class Stick:
    def __init__(self, canvas, color, stickX, stickY, stickW, stickH):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, stickW, stickH, fill=color)
        self.canvas.move(self.id, stickX, stickY)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.speed = 4

    def turn_left(self, evt):
        print("turn_left")
        self.x = -self.speed

    def turn_right(self, evt):
        print("turn_right")
        self.x = self.speed

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
