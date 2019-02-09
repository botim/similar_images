# USAGE
# python detect_barcode.py --image images/barcode_01.jpg

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
ap.add_argument("-i", "--dir", required = True, help = "path to the dir")
args = vars(ap.parse_args())

directory=args["dir"]

#dst = cv2.CreateMat(40,30, cv2.CV_8U)

vis_debug = True
if vis_debug:
    cv2.namedWindow("ref")
    cv2.namedWindow("dup")
    cv2.namedWindow("debug")


use_local_disk = True
if use_local_disk:

    for ref_name in os.listdir(directory):
        if not (ref_name.endswith(".jpg") or ref_name.endswith(".png")):
            # print(os.path.join(directory, filename))
            continue
        #print('ref image is ' + ref_name)
        ref_image_name = os.path.join(directory, ref_name)
        ref_image = cv2.imread(ref_image_name)
        hash_value_1200_bytes = hash.image_to_hash(ref_image)
        ref_sig_150_chars = hash.thelve_hadred_bytes_to_150_chars(hash_value_1200_bytes)
        #print('ref_sig_150_chars is ' + ref_sig_150_chars)

        min_dist = 1200
        for filename in os.listdir(directory):
            if not (filename.endswith(".jpg") or filename.endswith(".png")):
                #print(os.path.join(directory, filename))
                continue
            else: # an iamge
                if (filename == ref_name):
                    continue
                #print('reading:' +  filename)
                # load the image and convert it to grayscale
                image_name = os.path.join(directory, filename)
                image = cv2.imread(image_name)

                hash_value_1200_bytes = hash.image_to_hash(image)
                sig_150_chars = hash.thelve_hadred_bytes_to_150_chars(hash_value_1200_bytes)

                score = hash.dist_signatures(ref_sig_150_chars, sig_150_chars)
                score = hash.hamming_dist_signatures(ref_sig_150_chars, sig_150_chars)


                if score < 5: # the value of almost similar depends on application
                    print('score {} vs {} = {}'.format(ref_name, filename, score))



                    print (filename + '=' +ref_name)

                    if vis_debug:
                        #similar_images = np.concatenate((ref_image, image), axis=1)
                        cv2.imshow("ref", ref_image)
                        cv2.imshow("dup", image)
                        cv2.waitKey(-1)

                if min_dist > score:
                    min_dist = score
        print('image  {} min dist ={}'.format(ref_name, min_dist))

print("done")
    # end all images
if vis_debug:
        cv2.destroyAllWindows()