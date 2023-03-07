import numpy as np
import datetime as datetime

class Impfpass:
    def __init__(self):
        self. _geimpft = False
        self._genesen = False
        self._getestet = datetime.datetime.now() - datetime.timedelta(hours=25)

    def _set_geimpft(self):
        self._geimpft = True
    
    def _set_genesen(self):
        self._genesen = True

    def _set_getestet(self):
        self._getestet = datetime.datetime.now()
    
    def einlass_erlaubt(self):
        wert=False

        if self._geimpft== True:
            wert= True
        elif self._genesen==True:
            wert=True
        elif self._getestet > datetime.datetime.now() - datetime.timedelta(hours=24):
            wert=True
        else:
            wert=False

        return wert

Person1 = Impfpass()

print(f'Der Enlass von Person1 ist gestattet (True) bzw. untersagt(False):{Person1.einlass_erlaubt()}.')


Person1._set_geimpft()
#Person1._set_genesen()
#Person1.einlass_erlaubt
print(f'Der Enlass von Person1 ist gestattet (True) bzw. untersagt(False):{Person1.einlass_erlaubt()}.')

