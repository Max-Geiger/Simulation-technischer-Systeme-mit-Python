import numpy as np
from WordProcess import WordCount as wp
import matplotlib.pyplot as plt

pathe='/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/Probeklausur 22/MyText_A.txt'

MainWords, WordCount = wp(pathe, key=True)
#print(MainWords,WordCount)

plt.bar(MainWords[0:5],WordCount[0:5])
plt.xlabel('Wört') # Achsenbeschriftung
plt.ylabel('Wörteranzahl') # Achsenbeschriftung
plt.title('Häufigste Wörter') #Titel
plt.grid() 
plt.xticks(rotation=45)
plt.show()
plt.savefig('PlotAufg2_A.png')