import math
x = input("Vuoi calcolare il volume del cubo - 1, o della sfera - 2? ")
if x == 1:
l = input("Inserisci il lato ")
   print "il volume del cubo e' ", l**3
else: 
   r = input("Inserisci il valore del raggio ")
   print "il volume della sfera e' ", (4.0*math.pi*r**3)/3.0
