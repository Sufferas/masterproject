import random
import json
import torch
from deepLearning.model_neural_net import NeuralNet

from deepLearning.nltk_utils import bag_of_words, tokenize


def get_trained_model(trained_model, json_file, input_string):

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    with open(json_file, 'r') as json_data:
        intents = json.load(json_data)

    FILE = trained_model
    data = torch.load(FILE)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    sentence = input_string
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(random.choice(intent['responses']))
                return True, random.choice(intent['responses'])
    else:
        print("No function could be connected to your input.")
        return False, "No function could be connected to your input."


# get_trained_model("TrainedModels/data.pth", "jsonFiles/intents.json", "hello")
# get_trained_model("TrainedModels/yes_no_data.pth", 'jsonFiles/yes_no.json', "yes")
