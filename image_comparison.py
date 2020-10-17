from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import PIL
from PIL import Image
import os

for filename in os.listdir('cropped_frames'):
    first_im_read=None
    if not filename.startswith('.'):
        for filenameception in os.listdir('cropped_frames/' + str(filename)):
            if filenameception.endswith('.jpg'):
                if(first_im_read is None):
                    first_im_read = cv2.imread("cropped_frames/" + str(filename) + '/' + str(filenameception), 0)
                    print("First" + str(first_im_read))
                    if not os.path.exists('different_frames'):
                        os.makedirs('different_frames')
                    if not os.path.exists("different_frames/" + "D" + str(filename)):
                        os.makedirs("different_frames/" + "D" + str(filename))
                    #cv2.imwrite("different_frames/" + "D" + str(filename) + '/' + str(filenameception), first_im_read)
                else:
                    print("First" + str(first_im_read))
                    new_im = cv2.imread("cropped_frames/" + str(filename) + '/' + str(filenameception), 0)
                    print("cropped_frames/" + str(filename) + '/' + str(filenameception))
                    print("Second" + str(new_im))
                    error = measure.compare_ssim(first_im_read, new_im)
                    print(error)
                    if error < 0.75:
                        cv2.imwrite("different_frames/" + "D" + str(filename) + '/' + str(filenameception), new_im)
