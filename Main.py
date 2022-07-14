import numpy as np
from Config import Config
from Mapper import Mapper
from KnnMain import knn_main
from DecissionTreeMain import dt_main
from RandomForestMain import rf_main
from BuildTeam import bt_main
class Main:
    def __init__(self, data_set_prefix):
        self.X = []
        self.Y = []
        self.config = Config(data_set_prefix)
        self.num_in_last = 0
        self.mapper = Mapper()
        self.load_data()

    def load_data(self):
        i = 0
        for csv_path in self.config.csv_files_names:
            csv_file = open(csv_path, "r")
            X_temp, Y_temp = self.mapper.map(csv_file)
            self.X.extend(X_temp)
            self.Y.extend(Y_temp)
            if i == len(self.config.csv_files_names)-1:
                self.num_in_last = len(Y_temp)
            i+=1

    def run_classifirs(self):
        self.classify_KNN()
        self.classify_DecissionTree()
        self.classify_RandomForest()

    def classify_KNN(self):
        len_x = len(self.X)
        idx = len_x-self.num_in_last
        X_test = self.X[idx:]
        X_base = self.X[:idx]
        Y_test = self.Y[idx:]
        Y_base = self.Y[:idx]
        knn_main(X_test, X_base, Y_test, Y_base, self.mapper)

    def classify_DecissionTree(self):
        len_x = len(self.X)
        idx = len_x-self.num_in_last
        X_test = self.X[idx:]
        X_base = self.X[:idx]
        Y_test = self.Y[idx:]
        Y_base = self.Y[:idx]
        dt_main(X_test, X_base, Y_test, Y_base)

    def classify_RandomForest(self):
        len_x = len(self.X)
        idx = len_x-self.num_in_last
        X_test = self.X[idx:]
        X_base = self.X[:idx]
        Y_test = self.Y[idx:]
        Y_base = self.Y[:idx]
        rf_main(X_test, X_base, Y_test, Y_base)

    def build_team(self):
        bt_main(self.mapper, self.X, self.Y)


if __name__ == "__main__":
    main = Main("Premier")
    main.run_classifirs()
    main.build_team()
