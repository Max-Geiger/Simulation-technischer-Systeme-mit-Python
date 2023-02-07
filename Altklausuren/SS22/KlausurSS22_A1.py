import matplotlib.pyplot as plt
import numpy as np





#infile = open(r'/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Altklausuren/SS22/F15_10.DAT','r')
#for line in infile:
    #print(line)
#    A = line
#print(A)
#    for row in reader:
#        print(row)
path = r'/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Altklausuren/SS22/F15_10.DAT'
A  = np.loadtxt(path, skiprows=3)
x = A[:,0]
x_oben = A[0:37,0]
x_unten = A[37:,0]
y = A[:,1]
y_oben = A[0:37,1]
y_unten = A[37:,1]
y_unten_interp = np.interp(x_oben,x_unten,y_unten)


print(A,x,y)

#plt.plot(x,y, label='Gesamtes Profil')
plt.plot(x_oben,y_oben, label='obere Profilschale', color='r')
plt.plot(x_unten,y_unten, label='untere Profilschale',color='g')
plt.fill_between(x_oben,y_oben,y_unten_interp)
plt.axis('equal')
plt.xlabel('x') # Achsenbeschriftung
plt.ylabel('y') # Achsenbeschriftung
plt.title('F15_10 Profilkontur') #Titel
plt.legend() 
plt.grid() 
plt.show()