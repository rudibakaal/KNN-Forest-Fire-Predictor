# KNN-Forest-Fire-Predictor

## Motivation
K-nearest neighbours algorithm designed to predict forest fire occurrence based on environmental data.

The dataset includes 244 instances compromising of 12 numeric enivornmental features and 1 binary class label of two forest regions in Algeria over a period of 4 months[1].


## KNN Results Summary
Sklearm's KNeighborsClassifier library was used with k=9 and the default Minkowski distance metric being used for this classification task. 

The KNN yields a F-score (which is the weighted average between precision and recall)[2] of .94.

![knn_conf_mat](https://user-images.githubusercontent.com/48378196/112323317-c8e90780-8d05-11eb-9ac5-44511d3851b3.png)

## License
MIT

## References
[1] Faroudja ABID et al. , Predicting Forest Fire in Algeria using Data Mining Techniques: Case Study of the Decision Tree Algorithm, International Conference on Advanced Intelligent Systems for Sustainable Development (AI2SD 2019) , 08 - 11 July , 2019, Marrakech, Morocco.
[2] https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
