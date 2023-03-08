import numpy as np
import matplotlib.pyplot as plt
import datetime 

class Impfpass:
    def __init__(self):
        self._geimpft = False
        self._genesen = False
        self._getestet = datetime.datetime.now() - datetime.timedelta(hours=25) 
    
    def _set_geimpft(self):
        self._geimpft=True

    def _set_genesen(self):
        self._genesen=True
    
    def _set_getestet(self):
        self._getestet=datetime.datetime.now()

    def einlass_erlaubt(self):
        a = False
        if self._geimpft:
            a=True
            print('Einlass gestattet, da geimpft')
        elif self._genesen:
            a=True
            print('Einlass gestattet, da genesen')
        elif self._getestet > datetime.datetime.now()-datetime.timedelta(hours=24):
            a=True
            print('Einlass gestattet, da in den letzten 24h getestet')
        else:
            print('Einlass nicht gestattet, da weder genesen, geimpft oder in den letzten 24h getestet')
        return a
    

Mensch1 = Impfpass()
#Mensch1._set_geimpft()
#Mensch1._set_genesen()
Mensch1._set_getestet()

Mensch1.einlass_erlaubt()
