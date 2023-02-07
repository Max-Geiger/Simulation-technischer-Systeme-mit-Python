import numpy as np


def crazy_function(number=7, new_list=[]): 

    """
    Ausgabe: bool_value: Überprüft ob number_sum gleich 41 ist 
    number_sum: Summe der Listeneinträge
    Monty: String Objekt mit dem Inhalt Monty
    """

    new_list.extend([number, number]) 
    new_list = new_list * 3
    number_sum = np.sum(new_list) 
    bool_value=number_sum==42
    #if number_sum == 42:
    #    bool_value=True
    #else:
    #    bool_value=False
    return [bool_value, number_sum, 'Monty']

ausgabe=crazy_function()
print(ausgabe)