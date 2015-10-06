#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Rename file.

Rename file to update time.
"""

import os
import time
import re

FILE_DIR = 'save'
BACKUP_DIR = 'rename_bk'
RENAME_PAT = '201[0-9][0-1][0-9][0-3][0-9].gif$'


def main():
    files = os.listdir(FILE_DIR)
    for f in files:
        file_path = os.path.join(FILE_DIR, f)
        org_file_name = os.path.basename(file_path)
        if re.match(RENAME_PAT, org_file_name):
            print 'Already changed file[{0}]'.format(org_file_name)
        f_stat = os.stat(file_path)
        update_epoc = f_stat.st_mtime
        update_time = time.gmtime(update_epoc)
        file_name = '{year}{month}{day}.gif'.format(
            year=update_time.tm_year,
            month=str(update_time.tm_mon).zfill(2),
            day=str(update_time.tm_mday).zfill(2))
        refile_path = os.path.join(FILE_DIR, file_name)
        if os.path.exists(refile_path):
            print 'Exist same file name[{0}].'.format(file_path)
            continue
        print file_path

# have change?
# Having dir?
# Rename (and backup?)

# How to write.
# os.rename()

if __name__ == '__main__':
    main()
