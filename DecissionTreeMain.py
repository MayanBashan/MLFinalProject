import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def dt_main(X_test, X_base, Y_test, Y_base):
    # dividing X, y into train and test data
    # X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state = 0)

    # training a DescisionTreeClassifier
    dtree_model = DecisionTreeClassifier().fit(X_base, Y_base)
    dtree_predictions = dtree_model.predict(X_test)

    # creating a confusion matrix
    cm = confusion_matrix(Y_test, dtree_predictions)
    disp = ConfusionMatrixDisplay(cm, display_labels=["Home Win", "Draw", "Away Win"])
    disp.plot()
    plt.show()
