#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of larry
# Copyright 2015 Neil Freeman
# all rights reserved

from __future__ import division
from random import randint
from moviepy.editor import VideoFileClip
from moviepy.editor import vfx
from .hasher import hamming_distance, hash_frame


def subclip(film, start=None, end=None, search_duration=None, **kwargs):
    '''
    return a subclip of a film between start and end, lasting at least search_duration
    '''
    search_duration = search_duration or 5 * 60

    # Pick a random place in a film, skipping the very start and end
    start = start or randint(30, int(film.duration) - 30)
    start = min(start, film.duration - 30)

    end = min(start + search_duration, film.duration)

    return film.subclip(start, end)


def find_clip(filename, min_length=None, max_length=None, **kwargs):
    """
    Returns VideoFileClip subclip object or None.
    Loops through film, one-half second at a time,
    looking at phashes trying to put together a 3+ second clip.
    :filename File to search
    :start start index in seconds
    :search_duration length of search in seconds
    :fraction search by <fraction> of a second
    :min_length minimum length of output clip, in seconds
    :max_length maximum length of output clip, in seconds
    """
    # fractions of a second to search by
    fraction = kwargs.pop('fraction', 2)

    # argument in seconds, convert to fractions of a second
    min_length = (min_length or 2) * fraction
    max_length = (max_length or 4) * fraction

    # cut up complete film
    complete = VideoFileClip(filename, audio=False)
    film = subclip(complete, **kwargs)

    buff = []

    # search film by fraction-of-a-second units
    for t in range(int(film.duration) * fraction):
        tc = t / fraction
        phash = hash_frame(film.get_frame(tc))

        try:
            dist = hamming_distance(buff[-1], phash)

        except IndexError:
            # If IndexError, we are at the start of the loop.
            # Add the hash and continue.
            buff.append(phash)
            continue

        # If max distance is exceeded,
        # either return a buffer that reaches min length or start search over.
        if dist > 6:
            if len(buff) > min_length:
                break
            else:
                buff = [phash]
                continue

        # If hash is close to previous hash, extend our buffer
        else:
            buff.append(phash)

        if len(buff) >= max_length:
            break

    if len(buff) > min_length:
        clipstart = tc - len(buff) / fraction + 1 / fraction
        clipend = tc - 1 / fraction

        # slow down slightly to make things more ponderous
        return film.subclip(clipstart, clipend).fx(vfx.speedx, 0.80)

    else:
        return None
