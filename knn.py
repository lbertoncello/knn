import sys
import numpy as np
import reading as rd
import writing as wt
import metrics as mt
import document as doc
import metrics as mt

def classify(train, u, k):
    calc_similarities(train, u)

    train.sort(key=lambda x: x.getSimilarity())
    k_nearest_neighbors = train[:k]

    classes = {}

    for neighbor in k_nearest_neighbors:
        if (neighbor.getDoc_class() in classes) == False:
            classes[neighbor.getDoc_class()] = 1
        else:
            classes[neighbor.getDoc_class()] += 1

    most_frequent_class = 0
    chosen_class = ''

    for c in classes:
        if classes[c] > most_frequent_class:
            most_frequent_class = classes[c]
            chosen_class = c

    return chosen_class

def calc_similarities(train, u):
    for vec in train:
        vec.setSimilarity(mt.euclidian_distance(vec.getDoc_vec(), u))

def create_train(train_file_name, classes_file_name):
    train = rd.read_vectors(train_file_name)
    classes = rd.read_classes(classes_file_name)

    train_objs = []

    for i in range(len(train)):
        train_objs.append(doc.Document(train[i], classes[i]))

    return train_objs

def main():
    train_filename = sys.argv[1]
    classes_filename = sys.argv[2]
    test_filename = sys.argv[3]
    k = int(sys.argv[4])

    train = create_train(train_filename, classes_filename)
    test = rd.read_vectors(test_filename)

    chosen_classes = []

    for i in range(len(test)):
        chosen_classes.append(classify(train, test[i], k))

    wt.write_results("results.txt", chosen_classes)

if __name__ == '__main__':
    main()