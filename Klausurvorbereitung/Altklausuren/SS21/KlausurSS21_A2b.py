import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from KlausurSS21_A1 import F
import pandas as pd


path='/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/SS21/A1.txt'
df = pd.read_csv(path, header=None)
a = float(df[0][0])
b = float(df[0][1])

def func(t,y):
    c1=1
    #c2=0.1
    b1=0.01
    b2=0.05
    m1=3
    m2=1

    c2=F(y[2],a,b)
    
    y1p=y[1]
    y2p=1/m1*(c2*y[2]-(c1+c2)*y[0]-b1*y[1])
    y3p=y[3]
    y4p=1/m2*(-b2*y[3]-c2*y[2]+c2*y[0])
    return y1p,y2p,y3p,y4p

sol1 = solve_ivp(func,t_span=(0,250),y0=[0,0,5,0])

plt.figure()
plt.subplot(1,2,1)
plt.plot(sol1.t,sol1.y[1,:],label='m1')

plt.legend()
plt.xlabel('Zeit') # Achsenbeschriftung
plt.ylabel('Geschwindigkeit') # Achsenbeschriftung
plt.grid() 

plt.subplot(1,2,2)
plt.plot(sol1.t,sol1.y[3,:],label='m2')
plt.legend()
plt.xlabel('Zeit') # Achsenbeschriftung
plt.ylabel('Geschwindigkeit') # Achsenbeschriftung
plt.grid() 


plt.tight_layout(pad=0.5) #subplotabstände
plt.show()


