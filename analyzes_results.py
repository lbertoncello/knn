from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import roc_auc_score

def analyze(correct_classes, predicted_classes):

	accuracy = accuracy_score(correct_classes, predicted_classes)

	precision_micro = precision_score(correct_classes, predicted_classes, average='micro')


	recall_micro = recall_score(correct_classes, predicted_classes, average='micro')

	f1_micro = f1_score(correct_classes, predicted_classes, average='micro') 
	f1_macro = f1_score(correct_classes, predicted_classes, average='macro')  

	#roc_auc = roc_auc_score(correct_classes, predicted_classes, average='micro')


	#return accuracy, precision_micro, recall_micro, f1_micro, f1_macro, roc_auc
	return accuracy, precision_micro, recall_micro, f1_micro, f1_macro