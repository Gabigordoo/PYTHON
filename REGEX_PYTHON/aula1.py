import re

string = "este édfdfum  12 2testefdf de expressões 212  regulares"
print(re.search(r'este', string))
print(re.sub(r'teste', 'ABC', string, count=0))
lista = "".join(re.findall(r'[0-9]+', string))
lista = "".join(re.findall(r'[^0-9]+', string))
print(lista)