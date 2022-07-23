import math
import numpy as np
from KNNClassifier import KNNClassifier
from MasksCreator import create_weak_knn_masks
from WeightedRule import WeightedRule
from WeightedVector import WeightedVector
import matplotlib.pyplot as plt


def ada_main(X_test, X_base, Y_test, Y_base, mapper):
    res = []
    for k in (5, 7, 11, 13):
        weak_knn_masks = create_weak_knn_masks(mapper)
        classifiers = []
        for mask in weak_knn_masks:
            classifiers.append(KNNClassifier(mask, k))
        adaboost = Adaboost(len(classifiers))
        weighted_rules = adaboost.run_adaboost(X_test, Y_test, X_base, Y_base, classifiers)
        res.append(adaboost.classify_weighted_rules(weighted_rules, X_test, Y_test, X_base, Y_base))
    show_results(res)

def show_results(ada_res):
    labels = ['K=5', 'K=7', 'K=11', 'K=13']
    avg_knn_res = [0.504, 0.507, 0.528, 0.536]

    x = np.arange(len(labels))  # the label locations
    width = 0.25  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, avg_knn_res, width, label='KNN')
    rects2 = ax.bar(x + width/2, ada_res, width, label='Adaboost')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Accuracy')
    ax.set_title('Classifier Accuracy')
    ax.set_xticks(x, labels)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    # fig.tight_layout()
    fig.set_figwidth(15)
    fig.set_figheight(8)
    plt.show()

class Adaboost:
    def __init__(self, r):
        self.r = r

    def run_adaboost(self, test_set_X, test_set_Y, base_set_X, base_set_Y, rules):
        rules = [WeightedRule(rule) for rule in rules]
        len_data = len(test_set_X)
        weighted_vectors = []
        weighted_rules = []
        for vec in test_set_X:
            weighted_vectors.append(WeightedVector(vec, 1 / len_data))
        for it in range(0, self.r):
            min_error_rule = None
            min_error = math.inf
            min_num_mistake = 0
            for rule in rules:
                weighted_error_sum = 0
                num_mistake = 0
                for i in range(len(weighted_vectors)):
                    weighted_vector = weighted_vectors[i]
                    vector = weighted_vector.vec
                    vec_class = rule.classifier.classify_single(vector, base_set_X, base_set_Y)
                    val = 0 if vec_class == test_set_Y[i] else 1
                    weighted_error_sum += (weighted_vector.weight * val)
                    num_mistake += val
                if min_error_rule is None or weighted_error_sum < min_error:
                    min_error = weighted_error_sum
                    min_error_rule = rule
                    min_num_mistake = num_mistake
            if min_error > 0.5:
                break
            min_error_rule_weight = 0.5 * math.log(((1 - min_error) / min_error))
            min_error_rule.weight = min_error_rule_weight
            sum_points_weights = 0
            for i in range(len(weighted_vectors)):
                weighted_vector = weighted_vectors[i]
                vector = weighted_vector.vec
                min_error_rule_p_class = min_error_rule.classifier.classify_single(vector, base_set_X, base_set_Y)
                power_sub = 1 if min_error_rule_p_class == test_set_Y[i] else -1
                power = (-min_error_rule_weight) * power_sub
                weighted_vector.weight = (weighted_vector.weight * (math.e ** power))
                sum_points_weights += weighted_vector.weight
            checkSum = 0
            for weighted_vector in weighted_vectors:
                weighted_vector.weight = weighted_vector.weight / sum_points_weights
                checkSum += weighted_vector.weight
            weighted_rules.append(min_error_rule)
        return weighted_rules

    def classify_weighted_rules(self, weighted_rules, test_set_X, test_set_Y, base_set_X, base_set_Y):
        errors = 0
        for i in range(len(test_set_X)):
            match = test_set_X[i]
            classification = self.Hk(weighted_rules, match, base_set_X, base_set_Y)
            val = 0 if classification == test_set_Y[i] else 1
            errors += val
        return (len(test_set_X) - errors) / len(test_set_X)

    def Hk(self, rules, match, base_set_X, base_set_Y):
        final_ans = [0, 0, 0]
        for rule in rules:
            ans = rule.classifier.classify_single(match, base_set_X, base_set_Y)
            final_ans[ans + 1] += rule.weight
        max_value = max(final_ans)
        index = final_ans.index(max_value)
        return index - 1
