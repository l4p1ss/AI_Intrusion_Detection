import pandas as pd
import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from data_names import *


def main():

    print("** loading training data...")
    df = pd.read_csv(r'data/kddcup.data', names=attribute_names)
    df = preprocessing.one_hot(df)
    df = preprocessing.map2major5(df)
    print("** training data loaded and processed")

    y = df["attack_type"].values
    X = df[features].values

    dt = DecisionTreeClassifier(criterion='entropy', splitter='random', max_depth=15, min_samples_leaf=6)
    dt = dt.fit(X, y)

    x_rf = dt.predict(X)

    print("** training set accuracy (PCC) --> ", round(accuracy_score(y, x_rf) * 100, 2), "%")

    print("** loading testing data...")
    df = pd.read_csv(r'data/kddcup.data.corrected', header=None, names=attribute_names)
    df = preprocessing.one_hot(df)
    df = preprocessing.map2major5(df)
    print("** testing data loaded and processed")

    X = df[features].values
    y = df['attack_type'].values
    y_rf = dt.predict(X)

    cm = confusion_matrix(y, y_rf)

    arr = [[0 for _ in range(5)] for _ in range(5)]

    for v, c in df['attack_type'].value_counts().items():
        for i in range(len(cm[v])):
            a = round(cm[v][i] / c * 100, 2)
            ab = str(a) + '%'
            arr[v][i] = ab

    print("** confusion matrix:")
    for s in arr:
        print(*s)

    print("** testing set accuracy (PCC) --> ", round(accuracy_score(y, y_rf) * 100, 2), "%")


if __name__ == '__main__':
    main()
