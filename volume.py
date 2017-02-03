import math
x = input("Vuoi calcolare il volume del cubo - 1, o della sfera - 2? ")
l = input("Inserisci il lato ")
if x==1 :
   print "il volume del cubo e' ", l**3
else : 
   print "il volume della sfera e' ", (4*math.pi*l**3)/3
