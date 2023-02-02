#Imports:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scipy.optimize as op
from scipy.integrate import solve_ivp
from scipy.integrate import odeint
#from math import *
#from openpyxl import load_workbook
from KlausurSS21_A1 import Funktion


# ode Solver mit ivp


# Einlesen der neuen Dateien
a=[]
infile = open('Curve_Fitting.txt','r')
for line in infile.readlines():
    a.append(float(line))
    #print(line)
infile.close()
#print(a,a[0],a[1])



# Parameterdefinition
c1 = 1
c2 = a[0]
b1 = 0.01
b2 = 0.05
m1 = 3
m2 = 1




# Definieren des Gleichungssystems
def func1(t,y):
    # Aufstellen des Gleichnungssystems
    y1p = y[1]
    y2p = c2/m1*y[2]-(c1+c2)/m1*y[0]-b1/m1*y[1]
    y3p = y[3]
    y4p = -b2/m2*y[1]-c2/m2*y[2]+c2/m2*y[0]
    return [y1p,y2p,y3p,y4p]

# Funktionsaufruf
sol1 = solve_ivp(func1,t_span=(0,250),y0=[0,0,5,0])

# Plotten

fig, (ax1,ax2) = plt.subplots(1,2, figsize=(8,6))

ax1.plot(sol1.t,sol1.y[2,:],label='$m_2$')
ax1.set_xlabel('Zeit')
ax1.set_ylabel('Streckung über Zeit')
ax1.grid()
ax1.legend()


ax2.plot(sol1.t,sol1.y[3,:]*m2,label='$m_2$')
ax2.grid()
ax2.set_xlabel('Zeit')
ax2.set_ylabel('Federkraft')
ax2.legend()

plt.tight_layout(pad=0.5) #subplotabstände
plt.show()