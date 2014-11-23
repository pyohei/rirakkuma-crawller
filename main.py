#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" 4kuma comic crawler

crawl 4kuma comic
"""

URL = "http://www.shufu.co.jp/contents/4kuma/"
TEST_MODE = True
FILE_DIR = "./save"
LOG_FILE = "rirakkuma.log"

import os
import re
import urllib2
from datetime import datetime
from HTMLParser import HTMLParser

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
    save_path = os.path.join(FILE_DIR, img_file)
    if os.path.exists(save_path):
        log("Already img file in save dir", img_file)
        return
    url = URL + img_path
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    page = response.read()
    f = open(save_path, "w")
    f.write(page)
    f.close()
    log("Fetch new image", img_file)
    return

def log(msg, append=""):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    f = open(LOG_FILE, "a")
    f.write("[%s] %s: %s\n" % (now, msg, append))
    f.close()

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
    main()
