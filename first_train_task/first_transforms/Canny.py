import numpy as np
import cv2
from matplotlib import pyplot as plt

import pathlib

cur_dir = str( pathlib.Path(__file__).parent.resolve() ) + '/'
out_dir = cur_dir + '/' + 'output/' 

name = 'Lenna.jpg'

img = cv2.imread(  cur_dir + name , cv2.IMREAD_GRAYSCALE )
edges = cv2.Canny(img,100,200)
cv2.imwrite( out_dir + 'Canny_'+ name, edges)