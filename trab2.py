from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler



def processo(data,test_tamanho):
    train_data,test_data, train_target,test_target = train_test_split(data.data, data.target,
    test_size=test_tamanho, random_state=0,shuffle=True) 

    scaler = StandardScaler()

    scaler.fit(train_data)

    train_transformed = scaler.transform(train_data)
    test_transformed  = scaler.transform(test_data)

 

iris = datasets.load_iris()
wine = datasets.load_wine()
cancer = datasets.load_breast_cancer()

processo(iris,0.2)



print('targets iris: ',iris.target_names)
print('targets wine: ',wine.target_names)
print('targets cancer: ',cancer.target_names)