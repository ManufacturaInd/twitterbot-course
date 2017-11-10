

* settings.py: twitter and mastodon credentials
* post.py: make a post
* utils.py: helper functions


# Antes de começar

Antes de mais nada, é preciso copiar o ficheiro `settings.py.sample` para `settings.py`.

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

# TODO

* Testar credenciais do twitter
* `download_file('https://framacalc.org/9U2ilGfIBr.csv', 'dados.csv')`

CSV Infomed: sacar o excel em <http://app7.infarmed.pt/infomed/pesquisa.php>

    iconv -f ISO-8859-15 -t utf-8 lista_infomed.csv > infomed.csv
    sed -i 's/^M//' infomed.csv
    awk -F ";" '{print $2}' infomed.csv | sed 's/"//g' | sort | uniq | grep 'x$' | wc -l

* [Awk em CSV](https://www.joeldare.com/wiki/using_awk_on_csv_files)
