from screencappy.mylog import mylog, myerr
from screencappy.image_cap import create_image

from io import BytesIO
from os.path import getsize
from pathlib import Path
import subprocess
from tempfile import NamedTemporaryFile


        # import IPython; IPython.embed()

IMAGE_FORMAT_OPTIONS = ('png', 'jpg', 'tiff', 'pdf')


def is_valid_image_format(fmt):
    return fmt in IMAGE_FORMAT_OPTIONS

def screencapture_image_to_path(target_path, image_format):
    """
    Not intended to be called directly from CLI.

    target_path: in most usecases, target_path is a tempfile path
    """
    cmdparts = ["screencapture",
        "-d",    # display errors to the user graphically
        "-i",   # capture screen interactively
        "-o",   # in window capture mode, do not capture the shadow of the window
        "-r",   # do not add dpi meta data to image
        "-s",   # only allow mouse selection mode
        "-t",   # image format (pdf, jpg, tiff)
        image_format,
        "TARGET_PATH",
    ]
    cmdstr = ' '.join(cmdparts)
    myerr(cmdstr)
    cmdparts[-1] = target_path

    subprocess.call(cmdparts)


def screencapture_image_to_tempfile(image_format):
    """
    image_format is a str, e.g. in IMAGE_FORMAT_OPTIONS

    Returns: BytesIO object
    """
    tempfile = NamedTemporaryFile(suffix=f'.{image_format}', delete=False)
    screencapture_image_to_path(tempfile.name, image_format)
    if not getsize(tempfile.name):
        raise RuntimeError("No screenshot data was captured")
    else:
        imgdata = Path(tempfile.name).read_bytes()
        bx = BytesIO(imgdata)
        return bx

def capture_image(target_path, image_format):
    target_path = Path(target_path)
    imgfile = screencapture_image_to_tempfile(image_format)

    image = create_image(imgfile)
    # save image
    image.save(target_path, format=image_format)
    myerr(f"Wrote {getsize(target_path)} bytes to {target_path}")


def video_screencapture():
    """
    screencapture -R 0,0,400,300  -v /tmp/foomov.mp4

    """
    pass


