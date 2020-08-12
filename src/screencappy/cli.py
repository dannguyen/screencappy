import click
from time import sleep

from screencappy.mylog import mylog, myerr
from screencappy.capture import IMAGE_FORMAT_OPTIONS, capture_image, is_valid_image_format


# @click.argument("output-path", nargs=1, type=click.Path(dir_okay=False))
@click.command()
@click.argument("output-path", nargs=1, type=click.Path(dir_okay=False))
@click.option('-f', '--format',
                type=click.Choice(IMAGE_FORMAT_OPTIONS, case_sensitive=False),
                help='The image file format to output, if not obviously derived from [OUTPUT_PATH]'
                )
@click.option('-p', '--pause', type=click.FLOAT, default=1)
def main(output_path, format, pause):
    """ capture an image via screencapture """
    if not format:
        format = str(output_path).split('.')[-1].lower()
        if not is_valid_image_format(format):
            raise ValueError(f"Could not derive valid file format from {OUTPUT_PATH}; must be {IMAGE_FORMAT_OPTIONS}")

    if pause:
        myerr(f"Sleeping for {pause} seconds...")
        sleep(pause)
        capture_image(output_path, format)



if __name__ == '__main__':
    main()
