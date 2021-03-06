#!/usr/bin/env python2

import os
import os.path
import argparse
from termcolor import colored

from analizer import analize


parser = argparse.ArgumentParser(description='Analize media files for ' +
                                'detecting pornography.')

parser.add_argument('files', metavar='file', type=str, nargs='+',
                    help='File to analize.')

parser.add_argument('-R', action='store_const', const=True, default=False,
                    help='Analize recursively.')

parser.add_argument('-L', action='store_const', const=True, default=False,
                    help='Follow symbolic links.')

args = parser.parse_args()


def print_result(path, result):
    if result:
        print path + ": " + ' FUCK YEA'
    else:
        print path + ": " + 'NOT TODAY'


for file_ in args.files:

    file_ = os.path.expanduser(file_)

    if not os.path.exists(file_):
        print file_ + " doesn't exist."
        continue

    if not os.access(file_, os.R_OK):
        print file_ + " can't be read."
        continue

    if os.path.isdir(file_) and not args.R:
        print file_ + " is a folder, see -R option."
        continue

    if os.path.isdir(file_):
        for (dirpath, _, filenames) in os.walk(file_, True, None, args.L):
            for name in filenames:
                path = dirpath + "/" + name
                print_result(path, analize(path))
    else:
        print_result(file_, analize(file_))
