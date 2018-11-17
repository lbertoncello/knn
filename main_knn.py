from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn import datasets
import sys
import numpy as np
import reading as rd
import writing as wt
import metrics as mt
import document as doc
import metrics as mt
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from analyzes_results import analyze

def processo(estado,train_data,val_data):

	if estado:
		scaler = StandardScaler()

		scaler.fit(train_data)

		train_transformed = scaler.transform(train_data)
		val_transformed  = scaler.transform(val_data)

		return (train_transformed,val_transformed)
	else:
		return (train_data,val_data)

def test(train,test_data,k,vote_type):
	list_y  =list()

	for x in test_data:
		y = classify(train,x, k,vote_type)
		list_y.append(y)

	return list_y


def Grid_search(k_vec,data):
	skf = StratifiedKFold(n_splits=3)
	best = 0.1
	best_k = 0
	best_ponderado = ''
	best_z_score = False

	for k in k_vec:
		for ponderado in ['npo','po']:
			for z_score in [False,True]:
				soma = 0
				for trai_index,val_index in skf.split(X_train,y_train):
					X, X_val = data[trai_index], data[val_index]
					y, y_val = target[trai_index], target[val_index]

					X,X_val = processo(z_score,X,X_val)

					train = create_train(X,y)
					y_pred = test(train,X_val,k,ponderado)

					accuracy = accuracy_score(y_val,y_pred)

					soma = soma+accuracy
				soma = soma/3

				if soma > best:
					best = soma
					best_k = k
					best_ponderado = ponderado
					best_z_score = z_score

	return (best_k,best_ponderado,best_z_score)


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


def create_train(train, classes):
	train_objs = []

	for i in range(len(train)):
		train_objs.append(doc.Document(train[i], classes[i]))

	return train_objs


if __name__ == '__main__':

	array_k = [1,3,5,7]
	iris = datasets.load_iris()
	wine = datasets.load_wine()
	breast_cancer = datasets.load_breast_cancer()
	resultados = np.empty([10,6])
	nome_data = ''
	saida = list()

	for dataset in [iris,wine,breast_cancer]:
		i = 0
		data = dataset.data
		target = dataset.target

		if dataset == iris:
			nome_data = 'iris'
		else:
			if dataset == wine:
				nome_data = 'wine'
			else:
				nome_data = 'breast_cancer'

		params = list()

		skf = StratifiedKFold(n_splits=10)
		skf.get_n_splits(data, target)

		for train_index, test_index in skf.split(data,target):

		   X_train, X_test = data[train_index], data[test_index]
		   y_train, y_test = target[train_index], target[test_index]

		   k,ponderado,z_score = Grid_search(array_k,X_train)

		   X_train,X_test = processo(z_score,X_train,X_test)

		   train_data = create_train(X_train,y_train)

		   y_pred = test(train_data,X_test,k,ponderado)

		   scores = analyze(y_test,y_pred)
		   resultados[i] = np.copy(scores)
		   params.append((k,ponderado,z_score))
		   i=i+1
		   
		intervalo_confianca = np.std(resultados,axis=0)*2
		media = np.mean(resultados,axis=0)
		saida.append((nome_data,params,media,intervalo_confianca))


	print(saida)





   