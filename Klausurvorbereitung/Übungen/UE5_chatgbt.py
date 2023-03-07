import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

class PultrusionData:
    def __init__(self, filename):
        self.df = pd.read_csv(filename, sep=';',decimal=',',header=3, skiprows=[5])
        #df = pd.read_csv(file_path1, sep=';',decimal=',',header=3, skiprows=[5] )
        self.df = self.df[self.df['Dehnung 1'] >= 0] # Filter out negative Dehnung 1s
        
    def calculate_elastic_modulus(self):
        mask = (self.df['Dehnung 1'] >= 0.0005) & (self.df['Dehnung 1'] <= 0.0025)
        x = self.df['Dehnung 1'][mask]
        y = self.df['Zugspannung'][mask]
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        return slope
    
    def calculate_failure_load(self):
        return np.max(self.df['Zugspannung'])
    
    def plot_data(self, ax):
        ax.plot(self.df['Dehnung 1'], self.df['Zugspannung'], label='Data')
        mask = (self.df['Dehnung 1'] >= 0.0005) & (self.df['Dehnung 1'] <= 0.0025)
        x = self.df['Dehnung 1'][mask]
        y = self.df['Zugspannung'][mask]
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        ax.plot(x, slope * x + intercept, color='red', label='Regression')
        ax.set_xlabel('Dehnung 1')
        ax.set_ylabel('Zugspannung')
        ax.legend()
        
def plot_histogram(moduli, failure_loads):
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].hist(moduli, bins=5)
    axs[0].set_xlabel('Elastic Modulus')
    axs[0].set_ylabel('Count')
    axs[1].hist(failure_loads, bins=5)
    axs[1].set_xlabel('Failure Load')
    axs[1].set_ylabel('Count')
    plt.show()
    
def analyze_data(filenames):
    moduli = []
    failure_loads = []
    for filename in filenames:
        data = PultrusionData(filename)
        moduli.append(data.calculate_elastic_modulus())
        failure_loads.append(data.calculate_failure_load())
        fig, ax = plt.subplots(figsize=(8, 6))
        data.plot_data(ax)
        plt.show()
    plot_histogram(moduli, failure_loads)


path1='E:\Programme (HDD)\Python\Repository_Simulation teschnishcer Systeme\Simulation-technischer-Systeme-mit-Python\Klausurvorbereitung\Übungen\UE5_Specimen_RawData_1.csv'
path2='E:\Programme (HDD)\Python\Repository_Simulation teschnishcer Systeme\Simulation-technischer-Systeme-mit-Python\Klausurvorbereitung\Übungen\UE5_Specimen_RawData_2.csv'
path3='E:\Programme (HDD)\Python\Repository_Simulation teschnishcer Systeme\Simulation-technischer-Systeme-mit-Python\Klausurvorbereitung\Übungen\UE5_Specimen_RawData_3.csv'
path4='E:\Programme (HDD)\Python\Repository_Simulation teschnishcer Systeme\Simulation-technischer-Systeme-mit-Python\Klausurvorbereitung\Übungen\UE5_Specimen_RawData_4.csv'
path5='E:\Programme (HDD)\Python\Repository_Simulation teschnishcer Systeme\Simulation-technischer-Systeme-mit-Python\Klausurvorbereitung\Übungen\UE5_Specimen_RawData_5.csv'

filenames = [path1, path2, path3, path4, path5]
analyze_data(filenames)
