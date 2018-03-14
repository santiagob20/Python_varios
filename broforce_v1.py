# NOMBRE DEL PROGRAMA: Broforce
# AUTOR DEL PROGRAMA: Andrea Daza, Santiago Urintive, Sebastian Pinto

# LIBRERIAS
import simplegui

# CONSTANTES Y VARIABLES GLOBALES
LIENZO = [640, 400]
fondo = simplegui.load_image("https://www.dropbox.com/s/u4nouhlilcgm2rq/fondo1.png?dl=1")
fondo2 = simplegui.load_image("https://www.dropbox.com/s/6mx4hlkdmqn0d5m/fondo2.png?dl=1")
mi_personaje = simplegui.load_image("https://www.dropbox.com/s/vtwyhgsjo82w1gh/bigguy_final85.png?dl=1")
#villano = simplegui.load_image("https://www.dropbox.com/s/77lih042wdkg2lz/villano1.png?dl=1")
rambo = simplegui.load_image("https://www.dropbox.com/s/m82b8coswsal5fs/rambo_camina.png?dl=1")



# MANEJADORES DE EVENTOS
class Escenario:
    def __init__(self, posicion, escala):
        self.posicion = posicion
        self.escala = escala
            
class Escenografia(Escenario):
    def __init__(self, posicion, imagen, escala):
        Escenario.__init__(self, posicion, escala)
        self.imagen = imagen
        print(self.imagen)
        self.tamano = [self.imagen.get_width(), self.imagen.get_height()]
        print(self.tamano)
        self.centro = [self.tamano[0] // 2, self.tamano[1] // 2]
        print(self.centro)
    def draw(self, canvas):
        canvas.draw_image(self.imagen, self.centro, self.tamano, self.posicion, self.escala) 

class Escenografia_mov(Escenario):
    def __init__(self, posicion, imagen, escala):
        Escenario.__init__(self, posicion, escala)
        self.imagen = imagen
        print(self.imagen)
        self.tamano = [self.imagen.get_width(), self.imagen.get_height()]
        print(self.tamano)
        self.centro = [self.tamano[0] // 2, self.tamano[1] // 2]
        print(self.centro)
    def draw(self, canvas):
        self.posicion = [self.posicion[0] - 0.5,self.posicion[1]]    
        canvas.draw_image(self.imagen, self.centro, self.tamano, self.posicion, self.escala) 
        
class Personaje(Escenario):
    def __init__(self, imagen, posicion, escala, frames, fps):
        Escenario.__init__(self, posicion, [escala[0] // frames, escala[1]])
        self.imagen = imagen
        self.tamano = [self.imagen.get_width() // frames, self.imagen.get_height()]
        self.centro = [self.tamano[0] // 2, self.tamano[1] //2]
        self.frames = frames
        self.fps = fps
        self.tiempo = 0.0

    def draw(self, canvas):
        indice = (self.tiempo % self.frames) // 1
        centro_fotograma = [self.centro[0] +  indice * self.tamano[0], self.centro[1]]
        canvas.draw_image(self.imagen, centro_fotograma, self.tamano, self.posicion, self.escala) 
        self.tiempo += self.fps

# MANEJADOR DE DIBUJO
def draw_handler(canvas):
    capa0.draw(canvas)
    capa2.draw(canvas)
    p1.draw(canvas)
    #villano_.draw(canvas)
    rambo_.draw(canvas)

# REGISTRO DE CONTROLES Y OBJETOS
frame = simplegui.create_frame("Sprites", LIENZO[0], LIENZO[1])
frame.set_draw_handler(draw_handler)
frame.set_canvas_background("black")

capa0 = Escenografia_mov([320, 200], fondo, [fondo.get_width()-100, 400])
capa2 = Escenografia([320, 200], fondo2, [640, 400])
p1 = Personaje(mi_personaje, [310,220], [mi_personaje.get_width() // 2, mi_personaje.get_height() // 2], 85, 0.5)
#villano_ = Personaje(villano, [300,50], [villano.get_width(), villano.get_height()], 9, 0.1)
rambo_ = Personaje(rambo, [300,205], [1100, 100], 11, 0.103)

# INICIO
frame.start()

