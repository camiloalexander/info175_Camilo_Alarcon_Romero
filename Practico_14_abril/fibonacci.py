#funcion recursiva que calcule el n-esimo elemento de la susecion de fibonacci

#si n=0 0
#si n=1 1
#si n>1 F(n-1) + F(n-2)


def fibonacci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n > 1:
		return fibonacci(n-1) + fibonacci(n-2)
		

num = int(raw_input("Ingrese numero a calcular la susecion: "))
fib = fibonacci(num)
print fib

