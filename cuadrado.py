# -*- coding: utf-8 -*-

import turtle

def main():
	window= turtle.Screen()
	dave= turtle.Turtle()

	make_square(dave)
	turle.mainloop()

def make_square(dave):
	length=int(raw_input('Tamaño de cuadrado: '))
	make_line_and_turn(dave,100)

	for i in range(4):
		make_line_and_turn(dave,length)

def make_line_and_turn(dave,length):
	dave.forward(length)
	dave.left(90)

if __name__ == '__main__':
	main()