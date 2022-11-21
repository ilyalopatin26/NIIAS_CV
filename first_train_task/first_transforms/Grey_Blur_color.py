import cv2
import pathlib

cur_dir = str( pathlib.Path(__file__).parent.resolve() ) + '/'
out_dir = cur_dir + '/' + 'output/' 

def get_and_save_grayscale_image( name ):
    img = cv2.imread(  cur_dir + name , cv2.IMREAD_GRAYSCALE )
    cv2.imwrite( out_dir + 'grayscale_'+ name, img)
    print( img.shape ) #проверка одноканальности

def get_and_save_binarize_image (name, value ):
    img = cv2.imread( cur_dir + name )
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, value, 255, 0)    
    cv2.imwrite( out_dir + 'binarize_'+ name, img)

def gauss_blur( name, size ):
    img = cv2.imread( cur_dir + name )
    img_blur = cv2.GaussianBlur( img , (size, size ), 0)
    cv2.imwrite( out_dir + f'GaussBlur_{size}_'+ name, img_blur )

def median_blur( name, size):
    img = cv2.imread( cur_dir + name )
    img_blur = cv2.medianBlur(img, size)
    cv2.imwrite( out_dir + f'MedianaBlur_{size}_'+ name, img_blur )

def only_one_color ( name ):
    imag = cv2.imread( cur_dir + name )
    b, g, r = cv2.split(imag)
    cv2.imwrite( out_dir + 'blue_ch_'+ name, b )
    cv2.imwrite( out_dir + 'green_ch_'+ name, g )
    cv2.imwrite( out_dir + 'red_ch_'+ name, r )


name = 'Lenna.jpg'

get_and_save_grayscale_image( name )
get_and_save_binarize_image ( name, 130 )
gauss_blur( name, 11)
median_blur( name, 11)
gauss_blur( name, 5)
median_blur( name, 5)
only_one_color( name)
