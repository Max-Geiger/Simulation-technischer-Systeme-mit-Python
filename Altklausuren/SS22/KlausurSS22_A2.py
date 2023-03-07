import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#from scipy.integrate import odeint
from scipy import signal
m1 = 1
m2 = 0.01
c1 = 10
c2 = (m2/m1)*c1
c3 = 10000
d1 = 0.001
d2 = 0.005



# ode Solver mit ivp
def func0(t,y):
    y1p = y[1]
    y2p = -(d1+d2)/m1*y[1] + d2/m1*y[3] - (c1+c2+c3)/m1*y[0] + (c2+c3)*y[2] + ut*c1
    y3p = y[3]
    y4p = d2/m2*y[1] - d2/m2*y[3] + (c2+c3)/m2*y[0] - (c2+c3)/m2*y[2]
    return [y1p,y2p,y3p,y4p]

def ut(t):
    return signal.sqare(50*t)

def u2t(t):
    return (t//50)%2*100

#Wrapperfunktion
def bewegungsgleichung_weqpper(ut):
    def bewegungsgleichung(t,y):
        y1p = y[1]
        y2p = -(d1+d2)/m1*y[1] + d2/m1*y[3] - (c1+c2+c3)/m1*y[0] + (c2+c3)/m1*y[2] + ut*c1
        y3p = y[3]
        y4p = d2/m2*y[1] - d2/m2*y[3] + (c2+c3)/m2*y[0] - (c2+c3)/m2*y[2]
        return [y1p,y2p,y3p,y4p]
        
    return bewegungsgleichung



bewegungsgleihung_u1 = bewegungsgleichung_weqpper(ut)

sol1 = solve_ivp(bewegungsgleihung_u1,t_span=(0,50),y0=[0,0,0,0])
plt.plot(sol1.t,sol1.y[0,:],'o-',label='solve_ivp')
plt.legend()
plt.show()