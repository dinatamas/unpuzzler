#!/usr/bin/env python3
#
# Written by Marcix.
# Modified by dinatamas.
#
from argparse import ArgumentParser
from PIL import Image
from pwn import *


def main():
    argparser = ArgumentParser()
    argparser.add_argument('image')
    args = argparser.parse_args()

    img = Image.open(args.image)
    pixels = img.getdata()
    ungreened = []
    for px in pixels:
        if px[1] > 240 and px[2] < 10:
            # If the pixel is "green enough", make it white.
            ungreened.append((255, 255, 255))
        else:
            # Otherwise leave it as is.
            ungreened.append(px)

    # save modified image to other dir
    img.putdata(ungreened)
    img.save(args.image + '.new', "PNG")


if __name__ == '__main__':
    main()
