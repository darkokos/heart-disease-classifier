class Classifier:
    def __init__(self, X_test, y_test, model):
        self.__X_test = X_test
        self.__y_test = y_test
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    def fit(self, X_train, y_train):
        print(f'Training {self.__model.__class__.__name__}...')
        self.__model.fit(X_train, y_train)
        print(f'Finished training {self.__model.__class__.__name__}')

    def predict(self):
        print(f'{self.__model.__class__.__name__} predicting the classes in the test data set...')
        y_pred = self.__model.predict(self.__X_test)
        print(f'{self.__model.__class__.__name__} finished predicting the classes in the test data set')
        return y_pred
