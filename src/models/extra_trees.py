from sklearn.ensemble import ExtraTreesClassifier as Etc
import warnings
warnings.filterwarnings('ignore')


class ExtraTreesClassifier:
    def __init__(self):
        self.__model = Etc(random_state=42, n_jobs=1, warm_start=True, bootstrap=True, oob_score=True)
        self.__best_n_trees = 0

    @property
    def feature_importances_(self):
        return self.__model.feature_importances_

    def fit(self, X_train, y_train):
        best_oob_error = float('inf')

        for n_trees in [15, 30, 50, 100, 150, 200, 300, 400, 500, 600]:
            self.__model.set_params(n_estimators=n_trees)
            self.__model.fit(X_train, y_train)

            (n_trees, oob_error) = n_trees, 1 - self.__model.oob_score_

            if oob_error < best_oob_error:
                self.__best_n_trees, best_oob_error = n_trees, oob_error

        print(f'{self.__class__.__name__} found {self.__best_n_trees} trees provide the smallest error...')

    def predict(self, X_test):
        self.__model.set_params(n_estimators=self.__best_n_trees)
        return self.__model.predict(X_test)
