import numpy as np
import matplotlib.pyplot as plt

class Inertia:
    def __init__(self,fname,size):
        self._bitmap=np.genfromtxt(fname)
        self._length_px = size
        self._area_px = size**2
        self._distance_px = np.linspace(0,self._length_px-10,1)

    def show(self):
        plt.imshow(self._bitmap)
        plt.show()
    
    #center of gravity
    def get_cog(self): 
        return (10,10)
    
    def get_inertia(self):
        #_distance_px ()
        for i in range(self._bitmap):
            Iyi = self._length_px**4/12

        Iy = np.sum(Iyi)+np.sum(self._length_px**2*self._area_px*Iyi)
        Iz = Iy
        return Iy,Iz




path_etc = '/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/WiSe21/rect.csv'
path_gyroid = '/Users/maxgeiger/Documents/Simulation-technischer-Systeme-mit-Python/Klausurvorbereitung/Altklausuren/WiSe21/gyroid.csv'
etc = Inertia(path_etc,10)
gyroid = Inertia(path_gyroid,10)

etc.show()
etc_cog = etc.get_cog()
etc_inertia = etc.get_inertia()

gyroid.show()
gyroid_cog = gyroid.get_cog() 
gyroid_inertia = gyroid.get_inertia()


print(f'Der Massenschwerpunkt für das Bild "etc" liegt bei: {etc_cog:.2} und der das Trägehitsmoment {etc_inertia:.2}')
print(f'Der Massenschwerpunkt für das Bild "gyroid" liegt bei: {gyroid_cog:.2} und der das Trägehitsmoment {gyroid_inertia:.2}')