"""
Module description
@date: Mai 2020
@author: Hendrik Traub <h.traub@tu-bs.de>
@Copyright: 2020 TU Braunschweig
<www.tu-braunschweig.de>. All rights reserved.
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt


class Hole:
    """
    Hole describes a general hole
    """

    name = 'Hole'
    class_counter = 0

    def __init__(self):
        """
        Initialising an instance of the class hole sets the centre point of the hole at the coordinates (0/0)
        """
        Hole.class_counter += 1
        self._centre_point = (0, 0)
        pass

    @property
    def centre_point(self):
        """
        The centre point of the hole
        :return: _centre_point: tuple
        """
        return self._centre_point

    @centre_point.setter
    def centre_point(self, value):
        """

        :param value: tuple
        """
        self._centre_point = value


class Circle(Hole):
    """
    This class represents a circle
    """

    def __init__(self, radius):
        """

        :param radius: float
        """
        # Initialise protected attributes
        super().__init__()
        self._radius = 0.0
        self._radius_intended = 0.0

        # Set initial values
        self.radius = radius

    def __repr__(self):
        """
        How python shows an instance of type Circle
        :return: representation_string: str
        """
        representation_string = "Hole of type circle with radius: " + str(self._radius) + "mm"
        return representation_string

    def __add__(self, other):
        """
        Two circles are added by adding their area
        :param other: Circle
        :return: new_circle: Circle
        """
        new_area = self.area + other.area
        new_radius = np.sqrt(new_area/np.pi)
        new_circle = Circle(radius=new_radius)
        return new_circle

    @property
    def radius(self):
        """
        The radius of the circle
        :return: _radius: float
        """
        return self._radius

    @radius.setter
    def radius(self, value):
        """
        The radius of the circle
        :param value: float
        """
        self._radius = value

    @property
    def area(self):
        """
        The area of the circle
        :return: area: float
        """
        area = np.pi * self._radius ** 2
        return area

    @property
    def circumference(self):
        """
        The circumference of the circle
        :return: circumference: float
        """
        circumference = 2 * np.pi * self._radius
        return circumference

    @property
    def radius_intended(self):
        """
        The intended radius of the circle: may differ from the actual radius of the circle
        :return: _radius_intended: float
        """
        return self._radius_intended

    @radius_intended.setter
    def radius_intended(self, value):
        """
        The intended radius of the circle: may differ from the actual radius of the circle
        :param value: float
        """
        array_radii_intended = np.asarray(value)
        idx = (np.abs(array_radii_intended - 0.05 - self.radius)).argmin()
        self._radius_intended = array_radii_intended[idx]


class Square(Hole):
    """
    This class represents a square
    """

    def __init__(self, edge):
        """

        :param radius:
        """
        # Initialise protected attributes
        super().__init__()
        self._edge = 0.0

        # Set initial values
        self.edge = edge

    def __repr__(self):
        representation_string = "Hole of type square with edge: " + str(self.edge) + "mm"
        return representation_string

    def __add__(self, other):
        new_area = self.area + other.area
        new_edge = np.sqrt(new_area)
        new_circle = Square(edge=new_edge)
        return new_circle

    @property
    def edge(self):
        return self._edge

    @edge.setter
    def edge(self, value):
        self._edge = value

    @property
    def area(self):
        area = self.edge ** 2
        return area

    @property
    def circumference(self):
        circumference = 4 * self.edge
        return circumference


class HoleDetection:
    """
    Detects holes in an image.
    """
    def __init__(self, filepath, filename):
        """
        Purpose of the class
        :param filepath: str
        :param filename: str
        """
        self._filepath = filepath
        self._filename = filename
        self._image = None
        self._hole_list = []
        self._list_radius_intended = []

    @property
    def filename(self):
        return self._filename

    @property
    def filepath(self):
        return self._filepath

    @property
    def image(self):
        if self._image is None:
            # Reading Image
            image = cv2.imread(self.filepath + self.filename, 1)

            # Change from RGB to Gray Colour
            image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            self._image = cv2.medianBlur(image_grey, 5)

        return self._image

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

    def export_data(self):
        pass

