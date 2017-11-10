#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from utils import post_to_mastodon, post_to_twitter, download_file

POST_TO_MASTODON = False
POST_TO_TWITTER = False

post_content = ""

download_file('https://framacalc.org/9U2ilGfIBr.csv', 'dados.csv')


print(post_content)

if POST_TO_MASTODON:
    post_to_mastodon(post_content)

if POST_TO_TWITTER:
    post_to_twitter(post_content)
