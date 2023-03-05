#Imports:
#import numpy as np
#import matplotlib.pyplot as plt
from impfpass import create_customers 


class Restaurant:
    def __init__(self,name,seats,area) -> None:
        self._name = str(name)
        self._seats = int(seats)
        self._area = area
        self._customers=0
    
    @property
    def customers(self):
        print('Es befinden sich', self._customers, 'Kunden im Restaurant')
    @customers.setter
    def customers(self, value):
        self._customers = value

    @property
    def seats(self):
        print('Es sind noch', self._seats, 'Stühle frei.')
    @seats.setter
    def seats(self, value):
        self._seats = value

    def activate_new_regulation(self, min_area_per_customer):
        self._seats = int(self._area/min_area_per_customer)
    
    def check_in(self,value):
        if value==True:
            if self._seats-self._customers>0:
                print('Access Granted')
                self._customers=+1
            else:
                print('Restaurant already full')
        else:
            print('Access Denied')






#Liste mit 60 Impfpässen
Kunden=create_customers(60)

Jolly_Banana_Time = Restaurant('Jolly Banana Time',60,100)
Sad_Banana_Time = Restaurant('Sad Banana Time',60,100)

Sad_Banana_Time.activate_new_regulation(10)


Jolly_Banana_Time.customers(Kunden)
Sad_Banana_Time.customers(Kunden)

Jolly_Banana_Time.customers
Jolly_Banana_Time.seats
Sad_Banana_Time.customers
Sad_Banana_Time.seats
