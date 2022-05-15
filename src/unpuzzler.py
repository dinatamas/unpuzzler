#!/usr/bin/env python3
from argparse import ArgumentParser

import cv2

from preprocess import detect_tiles
from utils import show


def main():
    # Parse command line arguments.
    argparser = ArgumentParser()
    argparser.add_argument('image', help='image file')
    argparser.add_argument('count', type=int, help='number of jigsaw pieces')
    args = argparser.parse_args()

    # Load the image file.
    image = cv2.imread(args.image)
    show(image)

    # High-level puzzle solver algorithm.
    tiles = detect_tiles(image, args.count)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
