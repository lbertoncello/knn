from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score
import numpy as np

def definir_valor(label,valor):
	if label == valor:
		return 1
	else:
		return  0

def binarizar(valor,true,pred):
	n= len(true)

	for i in range(n):
		true[i] = definir_valor(true[i],valor)
		pred[i] = definir_valor(pred[i],valor)

	return true,pred

def roc_multi_class(y_true,y_pred):
	unique = np.unique(y_true)
	
	matrix_true = np.empty([len(unique),len(y_true)])
	matrix_pred = np.empty([len(unique),len(y_true)])

	for i in range(len(unique)):
		y,z = binarizar(unique[i],np.copy(y_true),np.copy(y_pred))

		matrix_true[i] = np.copy(y)
		matrix_pred[i] = np.copy(z)
		
	return roc_auc_score(matrix_true,matrix_pred)

def analyze(correct_classes, predicted_classes):

	accuracy = accuracy_score(correct_classes, predicted_classes)

	precision_micro = precision_score(correct_classes, predicted_classes, average='micro')


	recall_micro = recall_score(correct_classes, predicted_classes, average='micro')

	f1_micro = f1_score(correct_classes, predicted_classes, average='micro') 
	f1_macro = f1_score(correct_classes, predicted_classes, average='macro')  

	roc_auc = roc_multi_class(correct_classes,predicted_classes)


	return accuracy, precision_micro, recall_micro, f1_micro, f1_macro, roc_auc
	#return np.array([accuracy, precision_micro, recall_micro, f1_micro, f1_macro])