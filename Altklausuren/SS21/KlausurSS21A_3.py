#Imports:
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
#import cv2
#import scipy.optimize as op
#from scipy.integrate import solve_ivp
#from scipy.integrate import odeint
#from math import *
#from openpyxl import load_workbook
#import pytest
#import webbrowser
import datetime

class Impfpass:
    def __init__(self):
        self._geimpft = False
        self._genesen = False
        self._getestet = datetime.datetime.now() - datetime.timedelta(hours=25)

    def einlass_erlaubt(self):
        einlass=False
        if self._geimpft:
            einlass= True
            print('Einlass gewährt, da geimpft')
        elif self._genesen:
            einlass= True
            print('Einlass gewährt, da genesen')
        elif self._getestet > datetime.datetime.now() - datetime.timedelta(hours=24):
            einlass= True
            print('Einlass gewährt, da innerhalb der letzten 24 h getestet wurde')
        else: 
            print('Einlass nicht gewährt, da weder genesen, geimpft oder in den letzen 24 h negativ getestet wurde')

        return einlass


    @property
    def _set_genesen(self):
        pass

    @_set_genesen.setter
    def filename(self, value):
        self._genesen = True
    
    @property
    def _set_geimpft(self):
        pass

    @_set_geimpft.setter
    def _set_geimpft(self, value):
        self._geimpft=True
    
    @property
    def _set_getestet(self):
        self.getestet=datetime.datetime.now()

    @_set_getestet.setter
    def _set_getestet(self,value):
        pass


MaxMustermann = Impfpass
test = MaxMustermann.einlass_erlaubt

print(test)
