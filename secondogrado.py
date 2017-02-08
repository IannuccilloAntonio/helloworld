import math
print("Calcolo delle equazioni di secondo grado ax^2 + bx + c = 0 ")
a = input("Inserisci il valore di a ")
b = input("Inserisci il valore di b ")
c = input("inserisci il valore di c ")

if a == 0 and b == 0 and c == 0:
	print "L'equazione e' indeterminata "
elif a == 0 and b == 0:
        print "L'equazione e' impossibile "
elif a == 0:
        x= float(-c)/float(b)
	print "x vale ", x
else: 
	delta = (b**2) - (4.0*a*c)
	if delta > 0: 
    		x1 =  (float(-b) + math.sqrt(delta))/2.0*a
		x2 =  (float(-b) - math.sqrt(delta))/2.0*a
		print "x1 vale ", x1 , "x2 vale ", x2
	elif delta == 0:
		x = -b/(a*2.0)
		print "x vale = ", x
	else:
		print "L'equazione non ammette soluzioni "
