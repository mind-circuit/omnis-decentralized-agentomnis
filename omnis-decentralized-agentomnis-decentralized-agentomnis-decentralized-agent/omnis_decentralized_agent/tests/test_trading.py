import unittest
import numpy as np
from modules.defi_agents.predictive_modeler import PredictiveModeler

class TestPredictiveModeler(unittest.TestCase):
    def setUp(self):
        self.modeler = PredictiveModeler()

    def test_train_and_predict(self):
        X = np.array([[1], [2], [3], [4], [5]])
        y = np.array([5, 10, 15, 20, 25])
        self.modeler.train(X, y)
        prediction = self.modeler.predict(np.array([[6]]))
        self.assertTrue(len(prediction) == 1)

if __name__ == "__main__":
    unittest.main()
