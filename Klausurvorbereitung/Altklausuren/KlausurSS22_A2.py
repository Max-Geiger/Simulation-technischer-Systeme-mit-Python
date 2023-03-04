#Importieren von Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy import signal

#Implementierng der DGL

def DGl1(t,y):
    m1=1
    c1=10
    d1=0.001
    m2=0.01
    c2=c1*(m2/m1)
    d2=0.005
    u = 0.5*signal.square(np.pi*t*1/50)+0.5

    if t<300:
        c3=1000
    else:
        c3=0

    y1p=y[1]
    y2p=-(d1+d2)/m1*y[1]+d2/m1*y[3]-(c1+c2+c2)/m1*y[0]+(c2+c3)/m1*y[2]-c1*u
    y3p=y[3]
    y4p=d2/m2*y[1]-d2/m2*y[3]+((c2+c3)/m2)*(y[0]-y[2])
    return [y1p,y2p,y3p,y4p]

def DGL_wrap(u):
    def DGl(t,y):
        m1=1
        c1=10
        d1=0.001
        m2=0.01
        c2=c1*(m2/m1)
        d2=0.005
        c3=1000

        y1p=y[1]
        y2p=-(d1+d2)/m1*y[1]+d2/m1*y[3]-(c1+c2+c2)/m1*y[0]+(c2+c3)/m1*y[2]-c1*u
        y3p=y[3]
        y4p=d2/m2*y[1]-d2/m2*y[3]+((c2+c3)/m2)*(y[0]-y[2])
        return [y1p,y2p,y3p,y4p]

    return DGl

#def störung(t):
#    return 0.5*signal.square(np.pi*t*1/50)+0.5

#Funktion_u = DGL_wrap(störung)

sol1 = solve_ivp(DGl1,t_span=(0,600),y0=[0,0,0,0])

plt.figure()
plt.subplot(1,2,1)
plt.plot(sol1.t,sol1.y[0,:],'o-',label='solve_ivp')
plt.xlabel('t') # Achsenbeschriftung
plt.ylabel('Auslenkung') # Achsenbeschriftung
plt.title('m1') #Titel
plt.grid() 
plt.legend()


plt.subplot(1,2,2)
plt.plot(sol1.t,sol1.y[2,:],'o-',label='solve_ivp')
plt.grid() 
plt.xlabel('t') # Achsenbeschriftung
plt.ylabel('Auslenkung') # Achsenbeschriftung
plt.title('m2') #Titel

plt.tight_layout(pad=0.5) #subplotabstände 
plt.legend() 
plt.show()

