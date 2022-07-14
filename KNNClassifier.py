from collections import Counter
import numpy as np
from sklearn.neighbors import NearestNeighbors

class KNNClassifier:
    def __init__(self, mask, k):
        self.mask = mask
        self.k = k


    def classify(self, X_test, X_base, Y_test, Y_base):
        neigh = NearestNeighbors(n_neighbors=self.k)
        masked_base_set = self.mask.mask_base(X_base)
        neigh.fit(masked_base_set)
        t = 0
        correct = 0
        for test_vec in X_test:
            res = neigh.kneighbors([self.mask.mask(test_vec)], return_distance=False)
            votes = [Y_base[i] for i in res[0]]
            vote_result = Counter(votes).most_common(1)[0][0]
            if vote_result == Y_test[t]:
                correct += 1
            t += 1
        return correct/t
