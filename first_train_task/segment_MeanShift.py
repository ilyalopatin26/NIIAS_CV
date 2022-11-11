import numpy as np
import cv2
from sklearn.cluster import MeanShift, estimate_bandwidth
import pathlib

cur_dir = str( pathlib.Path(__file__).parent.resolve() ) + '/'
out_dir = cur_dir + '/' + 'output/' 

def MeanShift_segment ( name, blur_option = None ):
    img = cv2.imread( cur_dir + name )

    if blur_option is not None :
        if blur_option[0] == 'G':
            img = cv2.GaussianBlur(img, ( blur_option[1], blur_option[1] ), 0)
        if blur_option[0] == 'M':
            img = cv2.medianBlur(img, blur_option[1])

    flat_image = img.reshape((-1,3))
    flat_image = np.float32(flat_image)

    bandwidth1 = estimate_bandwidth(flat_image, quantile=.06, n_samples=3000)
    ms = MeanShift(bandwidth=bandwidth1, bin_seeding=True)
    ms.fit(flat_image)
    labeled=ms.labels_

    segments = np.unique(labeled)
    n_segment = segments.shape[0]

    total = np.zeros((segments.shape[0], 3), dtype=float)
    count = np.zeros(total.shape, dtype=float)
    for i, label in enumerate(labeled):
        total[label] = total[label] + flat_image[i]
        count[label] += 1
    avg = total/count
    avg = np.uint8(avg)

    
    res = avg[labeled]
    result = res.reshape((img.shape))

    cv2.imwrite( out_dir + 'MeanShift_'+ name, result )
    return n_segment

name = 'beach.jpg'

N = MeanShift_segment ( name, ['G', 11] )
print(N)