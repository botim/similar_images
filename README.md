# similar_images
Python code that compute a small signature for an image + comparison of two signatures
The core functionality is in hash_image_lib
The are 2 sample applications:
  * hash_url  - genrate a sample from a url of an image
  ^ has_dir  - for each image in a directory find the most similar image in the same directory (if similarity is small I.e., lees taht (hard code 5 out of 100 where "0" is identical images the images are displaied
  
  A couple of QA functions for self testing are provided in qa_lib
  
  
  Limitations: currently works only with 24bits (RGB) images 
  It will be nice if someone will help me connect to scrolling on url images. 
