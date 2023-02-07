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


    @property
    def genesen(self):
        pass

    @genesen.setter
    def genesen(self, value):
        self._genesen = True
    
    @property
    def geimpft(self):
        pass

    @geimpft.setter
    def geimpft(self, value):
        self._geimpft=True
    
    @property
    def getestet(self):
        self._getetste = datetime.datetime.now()

    @getestet.setter
    def getestet(self,value):
        if value:
            self._getestet = datetime.datetime.now()
    
    def einlass_erlaubt(self):
        einlass=False
        if self._geimpft:
            einlass = True
            print('Einlass gewährt, da geimpft')
        if self._genesen:
            einlass = True
            print('Einlass gewährt, da genesen')
        if self._getestet > datetime.datetime.now() - datetime.timedelta(hours=24):
            einlass = True
            print('Einlass gewährt, da innerhalb der letzten 24 h getestet wurde')
        else: 
            print('Einlass nicht gewährt, da weder genesen, geimpft oder in den letzen 24 h negativ getestet wurde')

        return einlass



MaxMustermann = Impfpass()
MaxMustermann.geimpft = True
MaxMustermann.genesen = True
MaxMustermann.getestet = True
MaxMustermann_Eintrittserlaubnis = MaxMustermann.einlass_erlaubt()

#test
