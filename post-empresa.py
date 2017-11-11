#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from utils import post_to_mastodon, post_to_twitter, download_file, get_csv_column_values

POST_TO_MASTODON = True
POST_TO_TWITTER = False

filename = download_file('https://framacalc.org/eCbVG6EF2x.csv', 'empresas.csv')

slogans = get_csv_column_values(filename, 'slogan')
names = get_csv_column_values(filename, 'nome')

slogan = random.choice(slogans)
name = random.choice(names)

post_content = slogan.replace('xxxxx', name)

print
print('  ' + post_content)
print

if POST_TO_MASTODON:
    post_to_mastodon(post_content)

if POST_TO_TWITTER:
    post_to_twitter(post_content)
