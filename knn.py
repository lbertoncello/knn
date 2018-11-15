import sys
import numpy as np
import reading as rd
import writing as wt
import metrics as mt
import document as doc
import metrics as mt

def choose_class_by_simple_vote(k_nearest_neighbors):
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

def calc_weight(document):
    return 1 / (document.getSimilarity() + 1)

def choose_class_by_weighted_vote(k_nearest_neighbors):
    classes = {}

    for neighbor in k_nearest_neighbors:
        if (neighbor.getDoc_class() in classes) == False:
            classes[neighbor.getDoc_class()] = calc_weight(neighbor)
        else:
            classes[neighbor.getDoc_class()] += calc_weight(neighbor)

    greater_weight = 0
    chosen_class = ''

    for c in classes:
        if classes[c] > greater_weight:
            greater_weight = classes[c]
            chosen_class = c

    return chosen_class

def classify(train, u, k, vote_type):
    calc_similarities(train, u)

    train.sort(key=lambda x: x.getSimilarity())
    k_nearest_neighbors = train[:k]

    if vote_type == 'po':
        return choose_class_by_simple_vote(k_nearest_neighbors)
    elif vote_type == 'npo':
        return  choose_class_by_weighted_vote(k_nearest_neighbors)

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
    vote_type = sys.argv[5]
    output_filename = sys.argv[6]

    train = create_train(train_filename, classes_filename)
    test = rd.read_vectors(test_filename)

    chosen_classes = []

    for i in range(len(test)):
        chosen_classes.append(classify(train, test[i], k, vote_type))

    wt.write_results(output_filename, chosen_classes)

if __name__ == '__main__':
    main()