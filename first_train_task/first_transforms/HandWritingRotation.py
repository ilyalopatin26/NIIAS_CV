
import numpy as np
import cv2
import pathlib
import copy

cur_dir = str( pathlib.Path(__file__).parent.resolve() ) + '/'
out_dir = cur_dir + '/' + 'output/' 


def rotation(img, C_rot, phi, sigma_x=1.0, sigma_y =1.0 ):
    m_zero = 1e-3
    if ( abs(sigma_x) < m_zero or  abs(sigma_y) < m_zero ):
        print("Impossible scale")
        return
    matrix_inv_scale = np.array( [ [ 1/sigma_x, 0 ], [ 0 , 1/sigma_y] ] )
    matrix_inv_rot = np.array( [ [np.cos(phi) , np.sin(phi) ], [-np.sin(phi), np.cos(phi)] ] )
    matrix_inv = matrix_inv_scale @ matrix_inv_rot
    rot_img = copy.deepcopy(img)
    x_size, y_size =rot_img.shape[0], rot_img.shape[1] 
    for x in range( x_size ) :
        for y in range( y_size ):
            vec = np.array([[x], [y]])
            vec1 = matrix_inv @ (vec-C_rot) + C_rot
            orig_x = int( vec1[0,0] )
            orig_y = int( vec1[1,0] )
            if( orig_x < 0 or orig_x >= x_size or orig_y < 0 or orig_y >= y_size   ):
                rot_img[x,y] = (0, 0, 0)
            else :
                rot_img[x,y] = img[ orig_x, orig_y] 
    cv2.imwrite( out_dir + 'rotHandWrite.jpg', rot_img )            


name = 'Lenna.jpg'

img = cv2.imread( cur_dir + name )


C_rot = np.array([ int(img.shape[0]/2) , int(img.shape[1]/2) ])
phi = np.pi/4
sigma_x = 0.5
sigma_y = 0.5

rotation( img, C_rot, phi, sigma_x, sigma_y)

