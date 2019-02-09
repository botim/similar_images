# USAGE
# python detect_barcode.py --image images/barcode_01.jpg

# import the necessary packages
import numpy as np
import math as math
import argparse
#import imutils
import cv2
import os
import urllib
import urllib.request


def imag_median(img):
    # COMPUTE HISTOGRAM OF SINGLE CHANNEL MATRIX
    nVals = 256
    hist = cv2.calcHist([img],[0],None,[nVals],[0,nVals] )
    hist = np.bincount(img.ravel(),minlength=256)

    #calcHist(&Input, 1, 0, cv::Mat(), hist, 1, &nVals, &histRange, uniform, accumulate);

    # COMPUTE CUMULATIVE DISTRIBUTION FUNCTION (CDF)
    median = 0
    sum = 0
    total = hist.sum()
    half_total = total/2
    for  i in range (nVals):
        sum = sum  + hist[i]
        if sum >= half_total:
            median = i-0.5

            return median

    print('reach max value :(  why ?')
    return median


def image_to_hash(image):
    # for visual debug replace resize and gary
    image_40_30 = cv2.resize(image, (40, 30))
    gray_40_30 = cv2.cvtColor(image_40_30, cv2.COLOR_BGR2GRAY)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_40_30 = cv2.resize(gray, (40, 30))

    t = imag_median(gray_40_30) - 1
    (_, thresh_img) = cv2.threshold(gray_40_30, t, 255, cv2.THRESH_BINARY)

    # visual debug
    # img_gray_bw = np.hstack((image_40_30, gray_40_30 ))
    img_gray_bw = np.concatenate((gray_40_30, thresh_img), axis=1)

    local_vis_debug = False
    if local_vis_debug:
        cv2.imshow("debug", img_gray_bw)
        cv2.waitKey(-1)

    hash_value_1200_bytes = thresh_img


    return  hash_value_1200_bytes

    # construct a closing kernel and apply it to the thresholded image
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    # closed = cv2.morphologyEx(thresh_img, cv2.MORPH_CLOSE, kernel)

    # perform a series of erosions and dilations
    # closed = cv2.erode(closed, None, iterations = 4)
    # closed = cv2.dilate(closed, None, iterations = 4)

def eghit_bytes_to_char(eghit_bytes):
    n = 0
    for i in range(8):
        factor = math.pow(2, i)
        b = eghit_bytes[7-i]
        if b == 1:
            n = n+factor


    s = chr(int(n))
    return(s)

def char_to_eghit_bytes(c):
    eghit_bytes =[0,0,0,0,0,0,0,0]

    n = ord(c)
    for i in range(8):
        factor = math.pow(2, 7-i)

        if n >= factor:
            eghit_bytes[i] = 1
            n = n - factor
        else:
            eghit_bytes[i] = 0
            n = n
    return(eghit_bytes)


def thelve_hadred_bytes_to_150_chars(bw_image):
#  Sry for the poor coding styal :(   We take hard coded in to acccont the 40X30 structure
# we encde every 4X 2  0/1 numbers --> a letter
# Therefore the 40X30 B/w pixels  ->  10X15 lettres
    signture =''

    data_win = np.array([4,2])
    for j in range(15):
        sy = j*2
        for i in range(10):
            sx = i * 4
            eight_masks = np.ravel([bw_image[sy, sx:sx+4], bw_image[sy+1, sx:sx+4]])
            #data_win[:, 0] = bw_image[sx:sx+4, sy]
            #data_win[:, 1] = bw_image[sx:sx+4, sy+1]
            #eight_bytes = np.reshape(data_win (1, np.product(data_win.shape)))
            eight_bytes = eight_masks / 255
            this_char = eghit_bytes_to_char(eight_bytes)
            signture = signture + this_char
        #print(signture)

    return(signture)



def hander_fifty_chars_to_1200_bytes(signture):
#  Sry for the poor coding styal :(   We take hard coded in to acccont the 40X30 structure
#  The invers fubction to the function above
    bw_image = np.arange(1200).reshape(40, 30)
    bw_image = np.zeros([30, 40], dtype=int)


    # mask = [255,255,255,255,255,255,255,255]
    # data_win = np.array([4,2])
    indx = 0
    for j in range (15):
        sy = j*2
        for i in range (10):
            sx = i * 4

            c = signture[indx]

            eight_bytes = char_to_eghit_bytes(c)
            #data_win = np.dot(np.array(eight_bytes), np.array(mask))
            data_win = np.dot(eight_bytes, 255)
            #print(data_win[0:4])
            #print(data_win[4:8])

            bw_image[sy, sx:sx + 4] = data_win[0:4]
            bw_image[sy+1, sx:sx + 4] = data_win[4:8]
            # invers of eight_masks =np.array([bw_image[sy, sx:sx+4], bw_image[sy+1, sx:sx+4]])
            indx = indx+1

    return(bw_image)


def dist_signatures(ref_sig_150_chars, sig_150_chars):
    n1 = len (ref_sig_150_chars)
    n2 = len(sig_150_chars)
    if n1 != n2:
        print ("bug :( len1 != len2 {} != {}".format(n1, n2))
        return (n1)


    score = 0
    for i in range(n1) :
        c1 = ref_sig_150_chars[i]
        c2 = sig_150_chars[i]
        if c1 != c2:
            score = score +1
    return (score)

def hamming_dist_signatures(ref_sig_150_chars, sig_150_chars):
    img1 = hander_fifty_chars_to_1200_bytes(ref_sig_150_chars)
    img2 = hander_fifty_chars_to_1200_bytes(sig_150_chars)
    haming_dist = dist_bw_img(img1, img2)
    dist = int(haming_dist/15)
    return(dist)  # units of % namely random is 50


def dist_bw_img(img1, img2):
    v1 = np.ravel(img1)
    v2 = np.ravel(img2)
    n1 = len(v1)
    n2 = len(v2)
    if n1 != n2:
        print ("bug :( len img1 != len img2 {} != {}".format(n1, n2))
        return (n1)


    score = 0
    for i in range(n1) :
        c1 = v1[i]
        c2 = v2[i]
        if c1 != c2:
            score = score +1
    return (score)
