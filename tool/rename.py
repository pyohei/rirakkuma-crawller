#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Rename file.

Rename file to update time.
"""

import os
import time
import re
import shutil
import logging

FILE_DIR = 'save'
BACKUP_DIR = 'backup_images'
RENAME_PAT = '201[0-9][0-1][0-9][0-3][0-9].gif$'


def main():
    """main module."""
    logging.basicConfig(format='[%(levelname)s] %(message)s',
                        level=logging.DEBUG)
    files = os.listdir(FILE_DIR)
    if not os.path.exists(BACKUP_DIR):
        os.mkdir(BACKUP_DIR)
    for f in files:
        file_path = os.path.join(FILE_DIR, f)
        org_file_name = os.path.basename(file_path)
        if re.match(RENAME_PAT, org_file_name):
            logging.info('Already changed file[{0}]'.format(org_file_name))
            continue
        # Get file name
        f_stat = os.stat(file_path)
        update_epoc = f_stat.st_mtime
        update_time = time.gmtime(update_epoc)
        file_name = '{year}{month}{day}.gif'.format(
            year=update_time.tm_year,
            month=str(update_time.tm_mon).zfill(2),
            day=str(update_time.tm_mday).zfill(2))
        refile_path = os.path.join(FILE_DIR, file_name)
        # Check file name
        if os.path.exists(refile_path):
            logging.info('Exist same file name[{0}].'.format(file_path))
            continue
        org_file_path = os.path.join(FILE_DIR, org_file_name)
        backup_file_path = os.path.join(BACKUP_DIR, org_file_name)
        shutil.copy(org_file_path, backup_file_path)
        shutil.copymode(org_file_path, backup_file_path)
        shutil.copystat(org_file_path, backup_file_path)
        new_file_path = os.path.join(FILE_DIR, file_name)
        os.rename(org_file_path, new_file_path)


if __name__ == '__main__':
    main()
