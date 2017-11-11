# Tweetbots!

Este é o código que serve de base à introdução aos Twitterbots que fizemos no
Date With Data de 10 de novembro de 2017.

# Antes de começar

Antes de mais nada, é preciso copiar o ficheiro `settings.py.sample` para `settings.py`.

E atenção que isto são scripts **Python 3**!

## Ativar Mastodon

1. Correr o `init_mastodon.py`
2. Preencher as informações que ele pede
3. Cortar e colar as linhas que ele nos dá para o `settings.py`

## Ativar Twitter

1. Ir a <https://apps.twitter.com/> depois de fazer login com a conta do nosso bot
2. Criar uma nova app
3. Ir a _Manage keys and access tokens_
4. Copiar os campos respectivos para o `settings.py`

Agora, no `post.py` podemos alterar os valores das variáveis `POST_TO_MASTODON`
e/ou `POST_TO_TWITTER` para `True`, e correr o script:

```bash
./post.py
```

