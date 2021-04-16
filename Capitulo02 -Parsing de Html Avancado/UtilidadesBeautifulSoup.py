from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen('https://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')


nameList = bs.findAll('span', {'class':'green'})# retira o texto da tag span de classe = green.
for name in nameList:
    print(name.get_text())

# argumento Text - faz correspondência com base no conteudo textual tags.
nameList2 = bs.find_all(text='the prince')
print(len(nameList2))

"""
find_all() - função que pode ser usada para extrair uma lista em Python,bastante flexível. 
           - filtra facilmente as páginas HTML e encontra as tags desejada. 
           
get_text() - funcão que remove todas as tags de um documento e devolve somente uma string Unicode.

Argumentos :
            1. tag
            2. attributes
            3. recursive
            4. text
            5. keywords
            6. limit
"""