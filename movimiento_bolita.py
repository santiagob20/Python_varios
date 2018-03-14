import simplegui

LIENZO = [400, 300]

class Bolita:
    def __init__(self,pos,dir,vel):
        self.pos = pos
        self.rad = 10
        self.dir = 0
        self.vel = 1
        

    def draw(self, canvas):
        canvas.draw_circle(self.pos,self.rad,2,'Green','Green')

    def mover(self):
        
        if(self.dir==1):
            self.pos[1] = self.pos[1] - self.vel
        if(self.dir==2):
            self.pos[0] = self.pos[0] + self.vel
            self.pos[1] = self.pos[1] - self.vel
        if(self.dir==3):
            self.pos[0] = self.pos[0] + self.vel
        if(self.dir==4):
            self.pos[0] = self.pos[0] - self.vel
            self.pos[1] = self.pos[1] + self.vel
        if(self.dir==5):
            self.pos[1] = self.pos[1] + self.vel
            #self.pos[1] = self.pos[1] + self.vel
        if(self.dir==7):
            self.pos[0] = self.pos[0] - self.vel
            #self.pos[1] = self.pos[1] - self.vel  
        
def draw_handler(canvas):
    mi_bolita.draw(canvas)
    mi_bolita.mover()
                                   
def key_down_handler(key):
    if(key == simplegui.KEY_MAP['up']):
        mi_bolita.dir = 1
    if(key == simplegui.KEY_MAP['down']):
        mi_bolita.dir = 5
    if(key == simplegui.KEY_MAP['left']):
        mi_bolita.dir = 7
    if(key == simplegui.KEY_MAP['right']):
        mi_bolita.dir = 3
    if(key==simplegui.KEY_MAP['z']):
        mi_bolita.vel = mi_bolita.vel + 1
                                   

frame = simplegui.create_frame("Traslación Simple", LIENZO[0], LIENZO[1])
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_down_handler)
                                   

mi_bolita = Bolita([200,150],0,2)

frame.start()