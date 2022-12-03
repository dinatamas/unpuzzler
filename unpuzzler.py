#!/usr/bin/env python3
from argparse import ArgumentParser
import os
import sys

from src.preprocess import preprocess_image


def main():
    # Parse command line arguments.
    argparser = ArgumentParser(description='the unpuzzler solves jigsaw puzzles')
    argparser.add_argument('input', help='directory with all piece images')
    args = argparser.parse_args()   

    # Preprocess each image.
    pieces = []
    if not os.path.exists(args.input):
        print(f'Path {args.input} does not exist', file=sys.stderr)
        sys.exit(1)
    if not os.path.isdir(args.input):
        print(f'Path {args.input} is not a directory', file=sys.stderr)
        sys.exit(2)
    try:
        for item in os.scandir(args.input):
            if item.is_file():
                pieces.append(preprocess_image(item.path))
    except PermissionError as e:
        print(f'{e.strerror}: {e.filename}', file=sys.stderr)
        sys.exit(3)
    if not pieces:
        print(f'Path {args.input} contains no images', file=sys.stderr)
        sys.exit(4)
    print(f'Loaded a total of {len(pieces)} pieces')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
