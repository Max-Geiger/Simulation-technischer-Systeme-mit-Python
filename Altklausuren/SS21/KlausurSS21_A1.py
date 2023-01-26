#Imports:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as op
from scipy.integrate import solve_ivp
#from scipy.integrate import odeint
#from math import *
#from openpyxl import load_workbook

#nutzen von Pandas zum Einlesen der Datei
columns = ["Weg", "Kraft"]
filepath = '/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Altklausuren/SS21/federkennlinie_klausur.csv'
df = pd.read_csv(filepath, sep=' ', delimiter=None, header=None)#, usecols=columns) 

# Speichern der Werte
x = df[0]
F = df[1]
#print(x,F)

# Curve-Fitting
def Funktion(x,a,b):
    return x/a*np.abs(np.tanh(x/b))

popt,pcov =op.curve_fit(Funktion,x,F)


plt.plot(x,F, 'x', color='green', label='gemessene Kraft')
plt.plot(x,Funktion(x,popt[0],popt[1]),'-.',label='fitting Funktion')
plt.xlabel('Weg') # Achsenbeschriftung
plt.ylabel('Kraft') # Achsenbeschriftung
plt.title('Curve-Fitting') #Titel
plt.legend(loc='lower right') 
Text = f'a={popt[0]:.1f} \nb={popt[1]:.1f}'
plt.text(-9.8,1.1, Text)
plt.grid() 
plt.show()



# Speichern der optimalen Daten in einer Textdatei
infile = open('Curve_Fitting.txt','w')
infile.write(str(popt))
infile.close()