import matplotlib.pyplot as plt


def show(img):
    """ Show an image in a window. """
    plt.imshow(img, cmap='gray')
    plt.show()
