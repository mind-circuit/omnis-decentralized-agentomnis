import numpy as np
from sklearn.linear_model import LinearRegression


class PredictiveModeler:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, X, y):
        print("TRAINING PREDICTIVE MODELER...")
        self.model.fit(X, y)

    def predict(self, X):
        print("PREDICTING MARKET TRENDS...")
        return self.model.predict(X)
