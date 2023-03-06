import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# a-----------------------------------
a=1
a1 = np.arange(1,11,1)
x = np.linspace(-3,3,50)
y = np.sign(x)

plt.figure(0)
plt.plot(x,y,'o-', label="Signum") #Hier werden die Werte zum Plotten übergeben
for i in range(len(a1)):
    y1 = np.tanh(a1[i]*x) 
    plt.plot(x,y1,'o-',label=f"Tanh, beta={a1[i]}")
plt.xlabel('x') # Achsenbeschriftung
plt.ylabel('y') # Achsenbeschriftung
plt.title('Vergleich Signung gegen tanh') #Titel
plt.legend() 
plt.grid() 
#plt.tight_layout(pad=0.5) #subplotabstände
#plt.show()

# b ------------------------------------


def func(t,y):
    k1=100
    k2=100
    m1=2
    m2=10
    g= 9.81
    mu1=0.2
    mu2=0.2
    f=0

    y1p = y[1]
    y2p = 1/m1*(-k1*y[0]-k2*(y[0]-y[2])-mu1*m1*g*np.tanh(1000*y[1])+f)
    y3p = y[3]
    y4p = 1/m2*(k2*(y[0]-y[2])-mu2*m2*g*np.sign(y[3]))

    return y1p,y2p,y3p,y4p

sol1 = solve_ivp(func,t_span=(0,15),y0=[-1,0,1,0], method='Radau')

plt.figure(1)
plt.plot(sol1.t,sol1.y[0,:],'-',label='m1')
plt.plot(sol1.t,sol1.y[2,:],'-',label='m2')
plt.xlabel('t') # Achsenbeschriftung
plt.ylabel('Auslenkung') # Achsenbeschriftung
plt.title('Lösung DGL') #Titel
plt.legend() 
plt.grid() 
#plt.show()

# c-----------------------------------

def func1(t,y):
    k1=100
    k2=100
    m1=2
    m2=10
    g= 9.81

    F=np.sin(2*np.pi*0.2*t)

    if t<300:
        mu1=0.2
        mu2=0.2
    elif 300<=t<=400:
        m1 = 0.2-0.2/0.05*t
        m2=m1
    elif t>400:
        mu1=0.5
        mu2=0.05
    else:
        pass

    y1p = y[1]
    y2p = 1/m1*(-k1*y[0]-k2*(y[0]-y[2])-mu1*m1*g*np.tanh(1000*y[1])+F)
    y3p = y[3]
    y4p = 1/m2*(k2*(y[0]-y[2])-mu2*m2*g*np.sign(y[3]))

    return y1p,y2p,y3p,y4p


sol2 = solve_ivp(func1,t_span=(0,500),y0=[0,0,0,0], method='Radau')

plt.figure(2)
plt.subplot(2,1,1)
plt.plot(sol2.t,sol2.y[0,:],'-',label='m1')
plt.subplot(2,1,2)
plt.plot(sol2.t,sol2.y[2,:],'-',label='m2')
plt.xlabel('t') # Achsenbeschriftung
plt.ylabel('Auslenkung') # Achsenbeschriftung
plt.title('Lösung DGL') #Titel
plt.legend() 
plt.grid() 
plt.show()
