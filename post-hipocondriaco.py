#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from utils import post_to_mastodon, post_to_twitter
from utils import pop_line_from_file

POST_TO_MASTODON = True
POST_TO_TWITTER = False

interjs = ["Carago", "Camandro", "Arreporra"]
interj = random.choice(interjs)
sintomas = ["-me constipado",
           " uma fraqueira",
           " uma obstipaçãozita",
           "-me febril",
           "-me um trapo",
           "-me todo roto",
           ]
sintoma = random.choice(sintomas)
farmaco = pop_line_from_file("nomes.txt")

post_content = "{}! Sinto{}, vou tomar um {}".format(interj, sintoma, farmaco)

print(post_content)

if POST_TO_MASTODON:
    post_to_mastodon(post_content)

if POST_TO_TWITTER:
    post_to_twitter(post_content)
