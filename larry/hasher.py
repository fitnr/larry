import sys
from PIL import Image
from moviepy.editor import VideoFileClip

"""
Generate hashes for a video file,
one for each frame at 25 FPS (which makes nice fractions)
"""

def hamming_distance(s1, s2):
    """
    Return the Hamming distance between equal-length sequences
    source: Wikipedia
    """
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")

    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def hash_frame(frame, resize=None):
    """
    Use PIL to hash a single image (frame).
    source: http://www.hackerfactor.com/blog/index.php?/archives/432-Looks-Like-It.html
    :frame array representation of the image
    :resize int number of pixels on each size of hash image
    """
    resize = resize or 8

    i = Image.fromarray(frame).resize((resize, resize), Image.ANTIALIAS).convert("L")

    pixels = list(i.getdata())
    avg = sum(pixels) / len(pixels)

    bits = "".join('1' if pixel < avg else '0' for pixel in pixels)
    hexadecimal = int(bits, 2).__format__('016x').upper()

    return hexadecimal


def hash_video(videofile, *args):
    video = VideoFileClip(videofile, audio=False).set_fps(25)
    return (hash_frame(frame, *args) for frame in video.iter_frames())


if __name__ == '__main__':
    hashes = hash_video(sys.argv[1])
    sys.stdout.writelines(h + '\n' for h in hashes)
