#!/usr/bin/env python3
# Noah Coffman
# source code: https://github.com/llSourcell/gender_classification_challenge/blob/master/demo.py
# Objective: Learn decision trees from sklearn
from sklearn import tree

clf = tree.DecisionTreeClassifier()


# [height, weight, shoe size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42],
     [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']


clf = clf.fit(X, Y)

prediction = clf.predict([[190,70,43]])

print(prediction)
