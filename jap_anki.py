import unicodecsv as csv

arquiv = open("Vocabulario.txt", "r", encoding="utf8")

matriz_palavras = list()

for line in arquiv:
    palavras = line.strip().split() # Separa por espaço
    
    jap = palavras[0] # Tira a palavra em japones

    lista_texto = list(jap) # Divide todos os caracteres em uma lista
    for index in range(len(lista_texto)): # Troca todos parenteses por conchetes para leitura em furigana no Anki
        if lista_texto[index] == "(":
            lista_texto[index] = "["
            if index - 1 != 0 and lista_texto[index - 2] != "]":
                lista_texto.insert(index - 1, " ")

        if lista_texto[index] == ")":
            lista_texto[index] = "]"

    jap = "".join(lista_texto) # Junta a lista em uma unica string

    palavra = " ".join(palavras[1:])

    palavra = [jap, palavra]

    matriz_palavras.append(palavra)# Toma cuidado para separar as palavras no arquivo

with open("Palavras_parsed.csv", "wb") as arquiv: # Abre arquivo em binario
    escrever = csv.writer(arquiv, quoting=csv.QUOTE_NONE, escapechar=' ')

    for linha in range(len(matriz_palavras)):
        palavra = matriz_palavras[linha] # Lista de string
        print(palavra)
        escrever.writerow([palavra[0], palavra[1]])


