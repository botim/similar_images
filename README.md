# similar_images
Python code that compute a small signature for an image + comparison of two signatures

# Algorithm
Based on a following pape: Sharing video annotations  Y. Caspi ; D. Bargeron  ICIP 2004. 
http://www.wisdom.weizmann.ac.il/~caspi/papers/ICIP04_final.pdf


The core functionality is in hash_image_lib
The are 2 sample applications:
  * hash_url  - genrate a sample from a url of an image
  ^ has_dir  - for each image in a directory find the most similar image in the same directory (if similarity is small I.e., lees taht (hard code 5 out of 100 where "0" is identical images the images are displaied
  
  * qa_lib - A couple of QA functions for self testing are provided in 
  
  # Limitations: 
  currently works only with 24bits (RGB) images 
  # TO DO:
  It will be nice if someone will help me connect to scrolling on url images. 
