import unittest
from titanic_notebook_refactoring_starter import prepare_data_and_train_models


class TestFunctional(unittest.TestCase):
    def test_prepare_data_and_train_model_should_return_accuracy_scores(self):
        scores = prepare_data_and_train_models()

        for score in scores:
            self.assertGreaterEqual(score, 70)
