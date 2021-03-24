import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report


# import dataset
ds = pd.read_csv('Algerian_forest_fires_dataset.csv')


# standardise features
s = StandardScaler()
for x in ds.columns:
    if x != 'Classes':
        ds[x] = s.fit_transform(ds[x].values.reshape(-1, 1)).astype('float64')


# create train & test variables
train,test = train_test_split(ds,test_size=.33)

train_labels = train.pop('Classes').values
test_labels = test.pop('Classes').values


# configure knn
neigh = KNeighborsClassifier(n_neighbors=9)
neigh.fit(train, train_labels)
predict = neigh.predict(test)


# results
classification_report = sklearn.metrics.classification_report(test_labels,predict)
print('classification_report:')
print(classification_report)

plot_confusion_matrix(neigh, test, test_labels)
plt.show() 