# Anki

Arquivos de automatização do processo de ensirir palabras/frase novas ao programa **Anki**.

## Japones
* Abre arquivo .txt
* Percorre casa linha
* Separa por espaço a linha
* Item 0 é a frase/palavra em japones
* Item 2 é a tradução
* Transforma item 0 em uma lista
  * Verifica se há parenteses na lista
    * Troca para colchetes para leitura do Furigana do Anki
    * Coloca espaço se proxima "letra" não for um Kanji
  * Junta a lista de volta
* Adiciona item 0 e item 1 numa lista "palavra"
* Adiciona lista "palavra" dentro de lista matriz_palavra
* Cria arquivo CSV
* Escreve cada linha da Variavel matriz_palavras no arquivo CSV.


## Russo
* Abre arquivo com "russo_anki.py python 0 (ou 1)"
* Percorre casa linha
* Se argv for 0 é uma frase completa 
  * Cria lista separada por "?" ou "."
  * Exclui itens vazios na lista
* Se argv diferente de 0 separa normalmente com split()
* Se len(lista) for maior que 2 temos 3 itens utéis
* * Adiciona item 0 e item 1 numa lista "palavra"
* Adiciona lista "palavra" dentro de lista matriz_palavra
* Cria arquivo CSV
* Escreve cada linha da Variavel matriz_palavras no arquivo CSV.

 ***Cuidado pra não misturar frases completas, palavras com fonetica e tradução e palavras com tradução em um só documento***
