import cv2


def preprocess_image(path):
    image = cv2.imread(path)
    return image
