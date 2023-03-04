#Imports:
import numpy as np
import matplotlib.pyplot as plt

Link = '/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/F15_10.DAT'
df = np.genfromtxt(Link,skip_header=3)
dfx = df[0:37,0]
dfy_o = df[0:37,1]
#dfx_u_interp = np.interp(df[0:37,0],df[37:,0],df[37:,1])
dfy_u_interp =  np.interp(df[0:37,0],df[37:,0],df[37:,1])
#print(df[:,0])
#print(dfx,dfy_o,dfy_u)
#equal

plt.plot(df[:,0],df[:,1],label="Konturdaten", color='r') #Hier werden die Werte zum Plotten übergeben 
plt.plot(df[0:37,0],df[0:37,1],label="Oberkante", color='g')
plt.plot(df[0:37,0],dfy_u_interp,label="Unterkante", color='b')
plt.fill_between(df[0:37,0],df[0:37,1],dfy_u_interp)
plt.xlabel('x') # Achsenbeschriftung
plt.ylabel('y') # Achsenbeschriftung
plt.title('Profilkontur') #Titel
plt.legend() 
plt.axis('equal')
plt.grid() 
plt.show()