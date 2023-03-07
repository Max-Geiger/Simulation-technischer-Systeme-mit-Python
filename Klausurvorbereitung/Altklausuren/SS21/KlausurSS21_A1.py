import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as op

file_path = '/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/SS21/federkennlinie_klausur.csv'
df = pd.read_csv(file_path,sep=' ',header=None)


def F(x,a,b):
    return x/a*np.abs(np.tanh(x/b))

popt,pcov =op.curve_fit(F,df[0],df[1])
print(popt[0],popt[1])

np.savetxt(r'/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/SS21/A1.txt', popt)#, fmt='%d')

plt.plot(df[0],df[1],'x',color='g',label="Messdaten") #Hier werden die Werte zum Plotten übergeben 
plt.plot(df[0],F(df[0],popt[0],popt[1]),'--',label="Curve Fitting")
plt.xlabel('Weg') # Achsenbeschriftung
plt.ylabel('Kraft') # Achsenbeschriftung
plt.title('Federkennlinie') #Titel
plt.legend(loc='lower right') 
plt.text(-9.9,1.1,f'a= {popt[0]:04.2}\nb= {popt[1]:0.3}')
plt.grid() 
plt.tight_layout(pad=0.5) #subplotabstände
plt.show()