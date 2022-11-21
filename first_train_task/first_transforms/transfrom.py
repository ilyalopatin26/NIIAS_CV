import cv2
import pathlib
import numpy as np #only panoram

cur_dir = str( pathlib.Path(__file__).parent.resolve() ) + '/'
out_dir = cur_dir + '/' + 'output/' 


def resizing( name, img , new_h, new_w, interpol_method=cv2.INTER_LINEAR ):
    res_img = cv2.resize(img, (new_h,  new_w), interpol_method )
    cv2.imwrite( out_dir + 'resize_'+ name, res_img)


def scale ( name, scale_h, scale_w , interpol_method=cv2.INTER_LINEAR ):
    img = cv2.imread( cur_dir + name )
    h, w = img.shape[:2]
    resizing ( name, img , int(h*scale_h), int(w*scale_w), interpol_method )


def rotation( img, name , angle, O, scale):
    (h, w) = img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D( O , angle , scale)
    rot_img = cv2.warpAffine(img, rotation_matrix, (w, h))
    cv2.imwrite( out_dir + 'rot_' + name, rot_img )

def double ( name1, name2 ): #work corect with only equal width sizes
    img = cv2.imread( cur_dir + name1 )
    img1 = cv2.imread( cur_dir + name2 )
    d_img = np.concatenate( (img, img1), axis =1 )     
    cv2.imwrite( out_dir + 'double_' + name,  d_img )

name = 'Lenna.jpg'
scale( name, 1, 2)
img = cv2.imread( cur_dir + name )
(h, w) = img.shape[:2]
center = ( h/2 , w/2 )
rotation( img, name, 45, center, 0.7 )
double (name, name)