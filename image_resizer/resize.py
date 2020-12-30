from pathlib import Path

from PIL import Image
import math

import logging


def resize(file_in, file_out=None, overwrite=False, target_size_bytes=10 ** 6):
    margin_percent = 8
    assert 0 < margin_percent < 100, "Margin needs to be less than 100%"
    file_out = file_out or file_in

    image = Image.open(file_in)

    x, y = image.size
    file_size_in_bytes = Path(file_in).stat().st_size

    while file_size_in_bytes > target_size_bytes:
        margin_percent += 1
        reduction = math.sqrt(target_size_bytes / file_size_in_bytes) - (margin_percent / 100)
        x2, y2 = math.floor(x * reduction), math.floor(y * reduction)
        image = image.resize((x2, y2), Image.ANTIALIAS)
        outpath = Path(file_out)
        if outpath.exists() and not overwrite:
            logging.warning('Output file exists and overwrite flag is not set. Skipping!')
        else:
            image.save(outpath, quality=95)
        file_size_in_bytes = Path(outpath).stat().st_size
    print(f'Converted {file_in} with a margin of {margin_percent}% resulting file size: {file_size_in_bytes}')

if __name__ == '__main__':
    file_in = r"C:\Users\Carl\PycharmProjects\image_resizer\image_resizer\test_data\resized\test_file3.HEIC"
    # file_in = Path(__file__).parent/'test_data'/'test_file3.HEIC'
    resize(file_in, 'test_out.jpg', overwrite=True)
    print(Path('test_out.jpg').stat().st_size)
