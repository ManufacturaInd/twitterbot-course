#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def post_to_mastodon(post_content):
    '''Faz um post no Mastodon. É preciso preencher os valores apropriados no settings.py.'''
    from mastodon import Mastodon
    from settings import MASTODON_CLIENT_ID, MASTODON_ACCESS_TOKEN, MASTODON_BASE_URL
    mastodon = Mastodon(
        client_id=MASTODON_CLIENT_ID,
        access_token=MASTODON_ACCESS_TOKEN,
        api_base_url=MASTODON_BASE_URL
    )
    mastodon.toot(post_content)


def post_to_twitter(post_content):
    '''Faz um post no Twitter. É preciso preencher os valores apropriados no settings.py.'''
    import tweepy
    from settings import TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_KEY, TWITTER_ACCESS_SECRET)
    api = tweepy.API(auth)
    success = False
    while not success:
        if api.update_status(status=post_content):
            success = True
        else:
            print("vou esperar 5 segundos e tentar de novo")
            time.sleep(5)


def is_proper_length(txt, limit=280):
    '''Diz se o texto tem um número de caracteres dentro do limite (280 por
    norma, que é o limite do Twitter)'''
    return len(txt) <= limit


def pop_line_from_file(filename, idx=None):
    '''Devolve uma linha de um ficheiro de texto e elimina-a desse ficheiro.'''
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    if not lines:
        return
    if idx or idx == 0:
        line = lines.pop(idx)
    else:
        line = lines.pop()
    new_file = open(filename, 'w')
    new_file.writelines(lines)
    new_file.close()
    return line.strip()


def download_file(url, filename):
    '''Faz download de um ficheiro para o nome indicado.'''
    import requests
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    with open(filename, "wb") as file:
        # get request
        response = requests.get(url, headers=headers)
        # write to file
        file.write(response.content)


def get_csv_column_values(csvfile, colname):
    '''Devolve uma lista de valores a partir de uma coluna de um ficheiro
    CSV.'''
    import unicodecsv as csv
    with open(csvfile, 'rb') as f:
        values = []
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            values.append(row[colname])
    return values
