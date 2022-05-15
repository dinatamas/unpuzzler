import cv2
import numpy as np
from scipy.ndimage import filters

from utils import show


# TODO: Avoid repeated contour searches?
def detect_tiles(image, count):
    """ Recognize puzzle piece contours and return their shapes. """
    # Adaptive threshold to differentiate color pixels from the background.
    # https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
    # Blurring helps when the tile edges blend in with the background.
    thresh = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)
    thresh = cv2.adaptiveThreshold(thresh, 255, 0, 1, 3, 3)
    thresh = cv2.GaussianBlur(thresh, (3,3), 1)
    show(thresh)

    # Detect the contours in the threshold image and keep the largest.
    # The largest contours will most likely correspond to the puzzle pieces.
    # The result is that all piece shapes are white, everything else is black.
    # https://docs.opencv.org/4.x/d4/d73/tutorial_py_contours_begin.html
    contours = cv2.findContours(thresh, 0, 1)[0]
    shapes = [[cnt.shape[0], i] for i, cnt in enumerate(contours)]
    largest = [contours[s[1]] for s in sorted(shapes, reverse=True)[:count]]
    rough = cv2.drawContours(np.zeros(image.shape[:2]), largest, -1, 255, cv2.FILLED)

    # Improve the sharpness of the detected contours.
    # The median filter will adjust outliers to fix small zigzags in the edges.
    # Find contours and draw black borders to undo the Gaussian blur.
    smooth = filters.median_filter(rough.astype('uint8'), size=10)
    trim_contours = cv2.findContours(smooth, 0, 1)[0]
    cv2.drawContours(smooth, trim_contours, -1, color=0, thickness=1)
    show(smooth)

