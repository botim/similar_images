# SAMPLE USAGE
# python --url https://pbs.twimg.com/media/Dyqy2J3XQAEvniI.jpg

# import the necessary packages
#import numpy as np
#import math as math
import argparse
#import imutils
import cv2
import os
import urllib
import urllib.request
import hash_image_lib as hash



# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--url", required = True, help = "path to the url of an image ")
args = vars(ap.parse_args())

url=args["url"]



vis_debug = True
if vis_debug:
    cv2.namedWindow("debug")


use_url = True
if use_url:
    #url = 'https://pbs.twimg.com/media/Dyqy2J3XQAEvniI.jpg'
    localName = '00000000.jpg'

    # :(
    #image=urllib.URLopener()
    #image.retrieve(url,localName)  # download comicName at URL



    urllib.request.urlretrieve(url, localName)

    print('download and reading:' + url)
    # load the image and convert it to grayscale

    image_from_url = cv2.imread(localName)

    hash_value_1200_bytes = hash.image_to_hash(image_from_url)

    sig_150_chars = hash.thelve_hadred_bytes_to_150_chars(hash_value_1200_bytes)
    print('Done url demo (data from):' + url)
    print(sig_150_chars)
    cv2.imshow("debug", image_from_url)
    cv2.waitKey(-1)



print("done")
    # end all images
if vis_debug:
        cv2.destroyAllWindows()