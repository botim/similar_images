'''

# Set of QA functions for internal lib functions

#1 test that   char --> 8bibts --> char   is statinary
# 2
'''
import argparse
#import imutils
import numpy as np
import cv2
import os
import urllib
import urllib.request
import hash_image_lib as hash

def test_char_to_8bits():
    isOK  = True
    for i in range (2,256):
        c = chr(i)
        bytes = hash.char_to_eghit_bytes(c)
        rc = hash.eghit_bytes_to_char(bytes)
        if c != rc :
                isOK = False
                print ( 'was={}  return{}'.format(c, rc))
    return(isOK)


def test_1200_bytes_to_sig():
        isOK = True
        int_array = np.random.randint(255, size=150)
        mystring = ''

        for digit in int_array:
                mystring = mystring + chr(digit)
        # QA
        print('encode ={}  '.format(mystring))

        bw_image = hash.hander_fifty_chars_to_1200_bytes(mystring)
        ret_signture = hash.thelve_hadred_bytes_to_150_chars(bw_image)
        if mystring != ret_signture :
                isOK = False
                print ( 'was={}  return{}'.format(mystring, ret_signture))
        return(isOK)



print("Start QA ")



isOK = test_1200_bytes_to_sig()
if isOK:
        print("test_1200_bytes_to_sig() is OK")
else:
        print("test_1200_bytes_to_sig() is FAIL :(")


isOK = test_char_to_8bits()
if isOK :
        print("test_char_to_8bits() is OK")
else:
        print("test_char_to_8bits() is FAIL :(")