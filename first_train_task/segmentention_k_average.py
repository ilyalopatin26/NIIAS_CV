import cv2
import numpy as np
import pathlib

cur_dir = str( pathlib.Path(__file__).parent.resolve() ) + '/'
out_dir = cur_dir + '/' + 'output/' 

name = 'beach.jpg'

orig_img = cv2.imread( cur_dir + name )

img =cv2.cvtColor( orig_img , cv2.COLOR_BGR2XYZ ) 

vectorized = img.reshape((-1,3))
vectorized = np.float32(vectorized)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

K = 2
attempts=10
ret,label,center=cv2.kmeans(vectorized,K,None,criteria,attempts,cv2.KMEANS_PP_CENTERS)

center = np.uint8(center)

res = center[label.flatten()]
result_image = res.reshape((img.shape))

cv2.imwrite( out_dir +'segment_'+ name, result_image )