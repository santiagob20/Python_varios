

def fiboRecursivo(n):
	if n<=1:
		return 1
	else:
		for i in range(0,n)
			fiboRecursivo(n-1)+fiboRecursivo(n-2)

	#return fiboRecursivo(n-1)+fiboRecursivo(n-2)

def run():
	n = int(raw_input('Ingrese  hasta que numero desea la sucesion: '))
	

	print 'El valor es:',fibo(n)

run()



























def fibonacci(n):
	while n>0:
		if n<=1:
			return 1
		else:
			return n-1+n-2

def run2():

	n = int(raw_input('Ingrese  hasta que numero desea la sucesion: '))
	print ' ',fibonacci(n)







def fibo(n):
fibonacci=[]
x=0
y=1
num=n
#num = int(raw_input("Numero de elementos:"))
for n in range(0,num):
	fibonacci.append(x+y)
   	aux = x + y
  	x = y
   	y = aux
	
def runnable():
	n = int(raw_input('Ingrese  hasta que numero desea la sucesion: '))
	fibo(n)


















def fiboDinamico(n):
	if n=1 || n=2:
		return 1
	if int(tabla[n])==0:
		tabla[n]=fiboDinamico(n-1)+fiboDinamico(n-2)
	return tabla[n]
	

def		
n = input('Ingrese el numero de la sucesion que quiere : ')
tabla[0:20]
print 'El valor es:',fiboDinamico(n)


