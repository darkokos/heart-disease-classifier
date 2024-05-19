import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

from keras.src.layers import Dense
from keras.src.metrics import Accuracy, F1Score, Precision, Recall
from keras.src.models import Sequential


class ArtificialNeuralNetwork:
    def __init__(self, input_size, X_valid, y_valid):
        self.model = Sequential([
            Dense(128, activation='relu', input_shape=(input_size,)),
            Dense(256, activation='relu'),
            Dense(128, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        self.model.compile(
            optimizer='adam',
            loss='binary_crossentropy',
            metrics=[Accuracy(), Precision(), Recall(), F1Score()]
        )

        self.X_valid = X_valid
        self.y_valid = y_valid

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train, batch_size=120, epochs=200, validation_data=(self.X_valid, self.y_valid))

    def predict(self, X_test):
        return (self.model.predict(X_test) > .5).astype(int)
