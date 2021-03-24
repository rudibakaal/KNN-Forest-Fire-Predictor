# KNN-Forest-Fire-Predictor

## Motivation
K-nearest neighbours algorithm designed to predict forest fire occurrence based on environmental data.

The dataset includes 244 instances compromising of 11 numeric enivornmental features and 1 binary class label of two forest regions in Algeria over a period of 4 months[1].


## KNN Results Summary
Sklearm's KNeighborsClassifier library was used with k=9 and the default Minkowski distance metric being used for this classification task. 

The KNN yields a F-score (which is the weighted average between precision and recall)[2] of .94.

![confusion_matrix_knn](https://user-images.githubusercontent.com/48378196/112314110-c1713080-8cfc-11eb-9072-4edadef10942.png)

## License
MIT

## References
[1] J.Czerniak, H.Zarzycki, Application of rough sets in the presumptive diagnosis of urinary system diseases,
Artifical Inteligence and Security in Computing Systems, ACS'2002 9th International Conference Proceedings,
Kluwer Academic Publishers,2003, pp. 41-51
[2] https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
