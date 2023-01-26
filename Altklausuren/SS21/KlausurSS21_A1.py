#Imports:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import scipy.optimize as op
from scipy.integrate import solve_ivp
#from scipy.integrate import odeint
#from math import *
#from openpyxl import load_workbook

#nutzen von Pandas
filepath = '/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/federkennlinie_klausur.csv'
df = pd.read_excel('federkennlinie_klausur.csv') 
print(df)
#df.to_dict()

#infile = open(federkennlinie_klausur.csv)
#for line in infile:
#    print(line)