#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" 4kuma comic crawler

crawl 4kuma comic
"""

URL = "http://www.shufu.co.jp/contents/4kuma/"
TEST_MODE = False
FILE_DIR = "./save"
LOG_FILE = "rirakkuma.log"
DETAIL_PATH = 'detail/detail.txt'
NOTIFICATION = True

import os
import re
import urllib2
from datetime import datetime
from HTMLParser import HTMLParser
import tweet


def main():
    if not os.path.exists(FILE_DIR):
        os.mkdir(FILE_DIR)
    if TEST_MODE:
        f = open("rirakkuma.html", "r")
        p = f.read()
        f.close()
    else:
        req = urllib2.Request(URL)
        response = urllib2.urlopen(req)
        p = response.read()
    rh = RilakkumaHTML()
    rh.feed(p)
    img_path = rh.get_img()
    img_file = img_path.split("/")[1]
    img_name = img_file.split('.')[0]
    save_path = os.path.join(FILE_DIR, img_file)
    if os.path.exists(save_path):
        __log("Already img file in save dir", img_file)
        return
    url = URL + img_path
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    f = open(save_path, "w")
    f.write(page)
    f.close()
    __log("Fetch new image", img_file)
    __save_detail(img_name)
    if NOTIFICATION:
        tweet.main()
    return


def __log(msg, append=""):
    """ Logging."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    f = open(LOG_FILE, "a")
    f.write("[%s] %s: %s\n" % (now, msg, append))
    f.close()


def __save_detail(image_name):
    """ Save file details to file.

    >>> __save_detail('200')
    """
    dir_name = os.path.dirname(DETAIL_PATH)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(DETAIL_PATH, 'a') as f:
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        line = '{name}, {time}\n'.format(name=image_name, time=now)
        f.write(line)


class RilakkumaHTML(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.imgs = ""

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for attr in attrs:
                if attr[0] == "src":
                    match = re.match(r"images\/[0-9]+\.gif", attr[1])
                    if match:
                        self.imgs = attr[1]

    def get_img(self):
        return self.imgs

if __name__ == "__main__":
    # main()
    import doctest
    doctest.testmod()
