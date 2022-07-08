from turtle import color
from display_image import *
import numpy as np

color_array = np.load("averages.npy")
img = create_image(color_array)

img.show()
 