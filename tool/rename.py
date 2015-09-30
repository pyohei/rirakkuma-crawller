#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Rename file.

Rename file to update time.
"""

import os
import time

FILE_DIR = 'save'


def main():
    files = os.listdir(FILE_DIR)
    for f in files:
        file_path = os.path.join(FILE_DIR, f)
        f_stat = os.stat(file_path)
        update_epoc = f_stat.st_mtime
        update_time = time.gmtime(update_epoc)
        file_name = '{year}{month}{day}'.format(
            year=update_time.tm_year,
            month=str(update_time.tm_mon).zfill(2),
            day=str(update_time.tm_mday).zfill(2))
        print file_name
# have change?
# Having dir?
# Rename (and backup?)

if __name__ == '__main__':
    main()
