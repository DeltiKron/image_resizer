import re
import sys
from argparse import ArgumentParser
from itertools import chain
from os import mkdir
from pathlib import Path

from image_resizer.resize import resize

parser = ArgumentParser()
parser.add_argument('folder_in')

args = parser.parse_args(sys.argv[1:])

folder_in = Path(args.folder_in)

folder_out = folder_in / 'resized'
if not folder_out.exists(): mkdir(folder_out)

input_extensions = ['jpg', 'JPG', 'JPEG', 'jpeg', 'png', 'PNG']

infiles = chain(*[folder_in.glob('*.' + extension) for extension in input_extensions])
for path_in in infiles:
    fn_out = re.sub(r'\.+$', '.jpg', path_in.name)
    resize(path_in, folder_out / fn_out, overwrite=True)
