print("Programma che calcola le equazioni di primo grado ax * b = 0")
a= input("Inserisci il valore di a ")
b = input("inserisci il valore di b ")

if a == 0 and b == 0: 
	print "il risultato dell'equazione e' indeterminato "
elif a == 0: 
	print "Il risultato dell'equazione e' impossibile "

else: 
	print "Il risultato dell'equazione e' ", -b/a
