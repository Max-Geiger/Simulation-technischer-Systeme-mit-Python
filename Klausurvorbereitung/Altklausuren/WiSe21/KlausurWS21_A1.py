#Imports:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



Dateipfad='/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/WiSe21/experimentalData.csv'
df = pd.read_csv(Dateipfad)
#print(df)
x=df['strain [-]']
y=df['force [uN]']
p = np.polyfit(x,y,4, full = True)

p0 = p[0]
LSE = float(p[1])
N=len(x)
f_max=max(y)

e=float(LSE/(N*f_max))
print(f'Das Polynom 4. Ordnung besitzt einen Fehler von {100*e:04.4} %')

x0=np.linspace(0,0.6,100)
y0=np.polyval(p0,x0)


#print(p0,LSE,N,f_max)
plt.plot(x,y, label="Experiment", color='tab:gray')
plt.plot(x0,y0, label="Fitting", color='k')
plt.xlabel('Dehnung') # Achsenbeschriftung
plt.ylabel('Kraft') # Achsenbeschriftung
plt.title('Experiment') #Titel
plt.legend() 
plt.grid() 
plt.show()