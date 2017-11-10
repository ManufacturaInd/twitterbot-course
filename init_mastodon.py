from mastodon import Mastodon
from getpass import getpass

USERNAME = raw_input("Nome de utilizador (Email)? ")
URL = raw_input("URL do Mastodon? ")
PASSWORD = getpass("Palavra-passe? ")
APPNAME = raw_input("Nome da app? (o nome do bot, tudo minúsculas) ")
# mastodon url?


credfile = "%s_credentials.secret" % APPNAME
loginfile = "%s_login.secret" % APPNAME
# get API key
Mastodon.create_app(APPNAME, api_base_url=URL, to_file=credfile)
# login and save user session (access token)
mastodon = Mastodon(client_id=credfile, api_base_url=URL)
mastodon.log_in(USERNAME, PASSWORD, to_file=loginfile)

print("Feito! Agora coloca estas linhas no teu settings.py:")
print
print('  MASTODON_CLIENT_ID = "%s"' % credfile)
print('  MASTODON_ACCESS_TOKEN = "%s"' % loginfile)
print('  MASTODON_BASE_URL = "%s"' % URL)
print
