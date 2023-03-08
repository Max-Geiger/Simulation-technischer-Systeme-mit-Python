import numpy as np
import matplotlib.pyplot as plt
import cv2
#import Image
from PIL import Image
from holes import Hole,Circle,Square



class HoleDetection:
    def __init__(self, filepath,filename):
        self._filepath=filepath
        self._filename=filename
        self._image=None
        self._hole_list=[]
        self._list_radius_intended = []
    
    def open(self):
        img = Image.open(self._filepath)
        img.show()
    
    def plot_radii(self):

        radii_list = []
        radii_intended_list = []

        for hole in self.hole_list:
            radii_list.append(hole.radius)
            radii_intended_list.append(hole.radius_intended)

        radii_array = np.asarray(radii_list)
        radii_intended_array = np.asarray(radii_intended_list)

        #plt.plot(radii_array, 'o')
        #plt.show()
        plt.plot(radii_intended_array, radii_array, 'o')
        plt.show()

    
    @property
    def filename(self):
        return self._filename
        
    @filename.setter
    def filename(self, value):
        self._filename = value
    
    @property
    def filepath(self):
        return self._filepath
    
    @filepath.setter
    def filepath(self,value):
        self._filename = value
    
    @property
    def image(self):
        if self._image is None:
            self._image = cv2.imread(self._filepath, 1)
            self._image = cv2.cvtColor(self._image,cv2.COLOR_BGR2GRAY)
            self._image = cv2.medianBlur(self._image,5)
        return self._image
    
    # @property
    # def image(self):
    #     if self._image is None:
    #         # Reading Image
    #         image = cv2.imread(self.filepath + self.filename, 1)

    #         # Change from RGB to Gray Colour
    #         image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #         self._image = cv2.medianBlur(image_grey, 5)

    #     return self._image
    
    # @property
    # def hole_list(self):
    #     if self._hole_list is None:
    #         self._hole_list = cv2.HoughCircles(self._image,cv2.HOUGH_GRADIENT,1,20,param1=60,param2=40,minRadius=0,maxRadius=0)
    
    @property
    def hole_list(self):

        if not self._hole_list:
            # Detect Circles
            circles = cv2.HoughCircles(self.image, cv2.HOUGH_GRADIENT, 1, 150, param1=500, param2=15, minRadius=0,
                                       maxRadius=50)
            radii_px = circles[0, :, 2]
            radii_mm = radii_px / 75.0

            if not self._list_radius_intended:
                print('Please write down the intended radii separated by spaces in micrometer')
                list_radius_intended = [int(x)/1000 for x in input().split()]
            else:
                list_radius_intended = self._list_radius_intended

            for radius in radii_mm:
                circle = Circle(radius=radius)
                circle.radius_intended = list_radius_intended
                self._hole_list.append(circle)

        return self._hole_list

        
filepath1='UE4_holes.JPG'
filename1='Bild1'
test1 = HoleDetection(filepath1,filename1)
test1.plot_radii()
