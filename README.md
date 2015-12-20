# larry

Create short, boring film clips.

Install with `python setup.py install`. Requires [Pillow](https://pypi.python.org/pypi/Pillow/2.1.0), which uses external libraries, so you may get an error without those. Tested on OS X and CentOS.

````
usage: larry [-h] [--max-length MAX_LENGTH] [--start START]
             [--granularity FRACTION] [-f {gif,mp4}] [-o OUTPUT]
             video

Create a short, boring film clip

positional arguments:
  video                 video file to use

optional arguments:
  -h, --help            show this help message and exit
  --max-length MAX_LENGTH
                        maximum length of clip
  --start START         time index to start search [default: random]
  --granularity FRACTION
                        higher values walk the film more carefully
  -f {gif,mp4}, --format {gif,mp4}
                        output format [default is mp4]
  -o OUTPUT, --output OUTPUT
                        save output file here [default is tmp]
````

## License

Copyright (c) 2015 Neil Freeman. All rights reserved.