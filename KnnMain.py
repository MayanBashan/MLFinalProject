from MasksCreator import create_weak_knn_masks
from KNNClassifier import KNNClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def knn_main(X_test, X_base, Y_test, Y_base, mapper):
    weak_knn_masks = create_weak_knn_masks(mapper)
    results = [[] for _ in weak_knn_masks]
    ks = [3, 5, 7, 9]
    for k in ks:
        print(f"|K = {k}|")
        i = 0
        for mask in weak_knn_masks:
            knn_classifier = KNNClassifier(mask, k)
            accuracy = knn_classifier.classify(X_test, X_base, Y_test, Y_base)
            results[i].append(accuracy)
            i += 1
            print(f"KNN = {knn_classifier.mask.name} | Accuracy = {accuracy}")
    plot_results(results, weak_knn_masks, ks)


def plot_results(matrix, weak_knn_masks, ks):
    columns = ks
    rows = [weak_knn_masks[i].name for i in range(len(matrix))]
    np_arr = np.array(matrix)
    df = pd.DataFrame(np_arr, columns=columns, index=rows)
    sns.heatmap(df, annot=True)
    # plt.pcolor(df)
    # plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
    # plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
    plt.show()
