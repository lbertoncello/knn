import numpy as np
import csv

#Le vetores em formato csv, separados por ' '
def read_vectors(file_name):
    with open(file_name, 'r') as csvfile:
        text = csv.reader(csvfile, delimiter=' ')

        vecs = list(text)

        num_of_lines = len(vecs)
        num_of_columns = len(vecs[0])

        docs = np.empty((num_of_lines, num_of_columns))

        for i in range(num_of_lines):
            docs[i] = np.array(vecs[i])

        return docs

#Le as classes, separadas por quebra de linha
def read_classes(file_name):
    file = open(file_name, 'r')
    text = file.readlines()
    file.close()

    classes = []

    for line in text:
        classes.append(line.replace('\n', ''))

    return classes