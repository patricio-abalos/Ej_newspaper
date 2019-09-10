import re
from collections import Counter
from newspaper import Article

def body(url):
    article = Article(url)
    article.download()
    article.parse()
    texto = article.text
    texto = texto.lower()
    d = re.split(r'\W+', texto)
    lista = Counter(d)
    print(lista)




