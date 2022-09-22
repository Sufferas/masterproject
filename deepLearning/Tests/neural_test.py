import unittest
from deepLearning.chat import *
import deepLearning.model_neural_net
import lib

class MyTestCase(unittest.TestCase):
    def test_yes_no_model_for_yes_1(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "yes")
        self.assertEqual(hit, True)
        self.assertEqual(output, "YES")

    def test_yes_no_model_for_yes_2(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "yes ")
        self.assertEqual(hit, True)
        self.assertEqual(output, "YES")

    def test_yes_no_model_for_yes_3(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "yes no")
        self.assertEqual(hit, False)

    def test_yes_no_model_for_yes_4(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "dont")
        self.assertEqual(hit, False)

    def test_yes_no_model_for_no_1(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "no")
        self.assertEqual(hit, True)
        self.assertEqual(output, "NO")

    def test_yes_no_model_for_no_2(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "thanks")
        self.assertEqual(hit, True)
        self.assertEqual(output, "NO")

    def test_yes_no_model_for_no_2(self):
        # from deepLearning.chat import get_trained_model
        hit, output = get_trained_model("../TrainedModels/yes_no_data.pth", '../jsonFiles/yes_no.json', "thinks")
        self.assertEqual(hit, False)


if __name__ == '__main__':
    unittest.main()

