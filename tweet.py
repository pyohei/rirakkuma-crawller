#!/usr/local/bin/python
# -*- coding: utf-8 -*-

""" Tweet rirrakuma 4kuma submit.

"""
import tweepy

TWEET_CONTENT = (
    "リラックマの4クマ漫画が更新されました！\n"
    "http://www.shufu.co.jp/contents/4kuma/"
    )
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""


def main():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth_handler=auth)
    api.update_status(status=TWEET_CONTENT)

if __name__ == '__main__':
    main()
