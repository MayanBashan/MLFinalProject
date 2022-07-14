from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

def rf_main(X_test, X_base, Y_test, Y_base):
    rf = RandomForestClassifier()
    rf.fit(X_base, Y_base)
    rf_predictions = rf.predict(X_test)
    cm = confusion_matrix(Y_test, rf_predictions)
    disp = ConfusionMatrixDisplay(cm, display_labels=["Home Win", "Draw", "Away Win"])
    disp.plot()
    plt.show()
