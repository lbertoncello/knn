# knn
kNN tradicional, implementado para a disciplina de Inteligência Artificial da UFES.

Execução:

    python3 knn.py [arquivo com os vetores de treino] [arquivo com as classes de cada um desses vetores, separadas por quebra de linha] [arquivo com os vetores a serem classificados] [valor de k] [método de votação] [nome do arquivo com os resultados]
  
Exemplo de execução:

    python3 knn.py train.txt classes.txt test.txt 3 po results.txt
  
Obs. 1: os arquivos de entrada devem estar todos em formato CSV, usando 1 espaço em branco (' ') como separador de colunas.

Obs. 2: a métrica utilizada é a de distância euclidiana.

Obs. 3: nos métodos de votação, 'po' é ponderada e 'npo' é não ponderada.
