import numpy as np

class Document(object):
    def __init__(self, doc_vec, doc_class):
        self.__doc_vec = doc_vec
        self.__doc_class = doc_class
        self.__similarity = -1

    def setSimilarity(self, similarity):
        self.__similarity = similarity

    def getSimilarity(self):
        return self.__similarity

    def getDoc_vec(self):
        return self.__doc_vec

    def getDoc_class(self):
        return self.__doc_class