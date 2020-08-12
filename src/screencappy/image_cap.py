#!/usr/bin/env python3
from io import BytesIO
from PIL import Image
from pathlib import Path

from screencappy.mylog import mylog, myerr

def create_image(fp):
    """
    fp is filepath or BytesIO

    returns Image object
    """
    image = Image.open(fp)
    # mylog(f"Create image; metainfo: {image.info}")
    # scrub metadata
    image.info = {}
    return image


def main():
    IMG_PATH = Path('tests/samples/images/lorem.png')
    imgbytes = IMG_PATH.read_bytes()
    imgio = BytesIO(imgbytes)
    import IPython; IPython.embed()



if __name__ == '__main__':
    main()
