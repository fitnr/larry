#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of larry
# Copyright 2015 Neil Freeman
# all rights reserved
import argparse
from . import larry
from . import hasher

__version__ = '0.1.0'


def main():
    format_choices = ('gif', 'mp4')

    parser = argparse.ArgumentParser(
        description='Create a short, boring film clip')

    parser.add_argument('video', type=str, help='video file to use')

    parser.add_argument('--max-length', default=4, type=int, help='maximum length of clip')

    parser.add_argument('--start', default=None, type=int,
                        help='time index to start search [default: random]')

    parser.add_argument('--granularity', default=4, dest='fraction', type=int,
                        help='higher values walk the film more carefully')

    parser.add_argument('-f', '--format', choices=format_choices, default='mp4',
                        type=str, help='output format [default is mp4]')

    parser.add_argument('-o', '--output', default=None, type=str,
                        help='save output file here [default is tmp]')

    args = parser.parse_args()

    # find clip, searches video starting from --time-index
    clip = larry.find_clip(
        args.video,
        start=args.start,
        max_length=args.max_length,
        fraction=args.fraction
    )

    if not clip:
        return

    # Save the file to a specific location or just a tmp file
    if args.output:
        dst = args.output

        if dst[-3:] not in format_choices:
            dst = dst + '.' + args.format
    else:
        dst = '/dev/stdout'

    # Writing to an io object doesn't work because moviepy is just a wrapper for ffpmeg
    # Write either gif or video
    if dst[-3:] == 'mp4':
        clip.write_videofile(dst, verbose=False)
    else:
        clip.write_gif(dst, loop=True, verbose=False)

if __name__ == '__main__':
    main()