import unicodecsv as csv
import re
import sys

arquiv = open("Vocabulario.txt", "r", encoding="utf8")

matriz_palavras = list()

for line in arquiv:
    palavras = line.strip() # Tira o \n do final

    if sys.argv[2] == 0:
        '''Use Anki.py python3 0 para frases completas'''
        palavras = re.split("[?.]", palavras) # Usando regular expression para colocar parametros de divisão de palavras/frases

        for i in palavras:
            if i == "":
                del i
    
    else:
        '''Use Anki.py python3 1 para palavras'''
        palavras = palavras.split()

        
    russ = palavras[0]

    if len(palavras) > 2:
        fonetica =  palavras[1]
        traducao = " ".join(palavras[2:])
        palavra = [russ, fonetica, traducao]

    else:
        traducao = palavras[1].strip()
        palavra = [russ, traducao]

    matriz_palavras.append(palavra) # Toma cuidado para separar as palavras no arquivo

with open("Palavras_parsed.csv", "wb") as arquiv: # Abre arquivo em binario

    escrever = csv.writer(arquiv, quoting=csv.QUOTE_NONE, escapechar=' ')

    for linha in range(len(matriz_palavras)):

        palavra = matriz_palavras[linha] # Lista de string
        print(palavra)

        if len(palavra) > 2:
            escrever.writerow([palavra[0], palavra[1], palavra[2]])

        else:
            escrever.writerow([palavra[0], palavra[1]])




