self.tk.update()
self.canvas_height = 500
self.canvas_width = 500
self.bg = PhotoImage(file="images/background.gif")
w = self.bg.width()
h = self.bg.height()
for x in range(0, 5):
    for y in range(0, 5):
        self.canvas.create_image(x*w, y*h, image=self.bg, anchor='nw')
    self.sprites = []
    self.running = True

def mainloop():
    while 1:
        if self.running == True:
            for srite in self.sprites:
                sprite.move()
                self.tk.update_idletasks()
                self.tk.update()
                time.sleep(0.01)