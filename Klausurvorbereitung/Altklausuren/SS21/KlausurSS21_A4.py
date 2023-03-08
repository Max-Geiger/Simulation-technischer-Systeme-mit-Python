import numpy as np
import matplotlib.pyplot as plt


def crazy_function(number=7,new_list=()): 
    """
    Ausgabe: bool_value: Überprüft ob number_sum gleich 41 ist number_sum: Summe der Listeneinträge
    Monty: String Objekt mit dem Inhalt Monty
    """
    new_list=new_list+(number, number)
    new_list = new_list * 3
    number_sum = np.sum(new_list) 
    bool_value = number_sum == 42
    return [bool_value, number_sum, 'Monty']

Ausgabe = crazy_function()
print(Ausgabe)
