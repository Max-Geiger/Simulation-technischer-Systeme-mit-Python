import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def funk(t,y):
    y1p=A1*np.exp(-E1/(R*y[1]))*y[0]**m*(1-y[0])**n
    y2p=1/cp*(qm*y1p+qsp)
    return (y1p,y2p)

A1=400
E1=18700
R=8.3
m=1.5
n=1.7
cp=1100
qm=84000
qsp=-142

#lsg_dgl
sol1 = solve_ivp(funk,t_span=(0,300),y0=[0.01,280],method='RK23')

alpha_p=A1*np.exp(-E1/(R*sol1.y[1]))*sol1.y[0]**m*(1-sol1.y[0])**n

#plt1
plt.subplot(3,1,1)
plt.plot(sol1.t,sol1.y[1,:],'o-',label='Temperatur',color='r')
plt.xlabel('t') # Achsenbeschriftung   
plt.ylabel('T') # Achsenbeschriftung
plt.title('Lösung DGL mittels solve_ivp_RK23') #Titel
plt.legend() 
plt.grid() 
#plt2
plt.subplot(3,1,2)
plt.plot(sol1.t,sol1.y[0,:],'o-',label='Aushärtegrad',color='b')
plt.xlabel('t') # Achsenbeschriftung
plt.ylabel(r'$\alpha$') # Achsenbeschriftung
plt.legend() 
plt.grid() 
#plt3
plt.subplot(3,1,3)
plt.plot(sol1.t,alpha_p,'o-',label='Aushärtungsrate',color='g')
plt.xlabel('t') # Achsenbeschriftung
plt.ylabel(r'$d\alpha/dT$') # Achsenbeschriftung
plt.legend() 
plt.grid() 

plt.tight_layout(pad=0.5) #subplotabstände
#plt.show()

#Aufgabenteil c

Startemperratur = np.arange(270,360,10)
t_ausgehärtet=[]
print(Startemperratur)
for T in Startemperratur:
    sol1 = solve_ivp(funk,t_span=(0,300),y0=[0.01,Startemperratur[T]],method='RK23')
    for i in range(len(sol1.y[0,:])):
        if sol1.y[1,i]==0.99:
            t_ausgehärtet.append(sol1.t[i])
        else:
            pass
    
print(t_ausgehärtet)

