#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Rename file.

Rename file to update time.
"""

import os
import time
import re

FILE_DIR = 'save'


def main():
    files = os.listdir(FILE_DIR)
    for f in files:
        file_path = os.path.join(FILE_DIR, f)
        org_file_name = os.path.basename(file_path)
# 正規表現チェックを


        
        f_stat = os.stat(file_path)
        update_epoc = f_stat.st_mtime
        update_time = time.gmtime(update_epoc)
        file_name = '{year}{month}{day}.gif'.format(
            year=update_time.tm_year,
            month=str(update_time.tm_mon).zfill(2),
            day=str(update_time.tm_mday).zfill(2))
        refile_path = os.path.join(FILE_DIR, file_name)
        if os.path.exists(refile_path):
            raise OSError('Exist same file name[{0}].'.format(file_path))
        print file_path
# have change?
# Having dir?
# Rename (and backup?)

if __name__ == '__main__':
    main()
