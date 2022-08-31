import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize
import csv


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
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

bot_name = "Sam"
print("Let's chat! (type 'quit' to exit)")
# while True:
#     # sentence = "do you use credit cards?"
#     sentence = input("You: ")
#     if sentence == "quit":
#         break
#
#     sentence = tokenize(sentence)
#     X = bag_of_words(sentence, all_words)
#     X = X.reshape(1, X.shape[0])
#     X = torch.from_numpy(X).to(device)
#
#     output = model(X)
#     _, predicted = torch.max(output, dim=1)
#
#     tag = tags[predicted.item()]
#
#     probs = torch.softmax(output, dim=1)
#     prob = probs[0][predicted.item()]
#     if prob.item() > 0.75:
#         print(prob.item())
#         for intent in intents['intents']:
#             if tag == intent["tag"]:
#                 print(f"{bot_name}: {random.choice(intent['responses'])}")
#     else:
#         print(prob.item())
#         print(f"{bot_name}: I do not understand...")

test_text = ["Ein besonderer Test", "welcher Spezifikation benötigt ein Unit Test beim schönem Wetter",
             "Zeit zum schlafen oder?","was machst du gerade?",
             "wir haben ein traumhaftes Wetter oder", "was machst du heute",
             "was soll ich mir kaufen","gibt es heute was Besonderes im Kino", "was benötige ich um ein Spiel zu spielen",
             "hello and bye"]


file = open('../../Sem2_project_master_arbeit/example_csv.csv', 'w')

with file:
    writer = csv.writer(file)
    writer.writerow(("ID", "Test Satz", "Genauigkeit 0.00 - 1", "Ausgabe des Chatbots"))

    id_num = 1
    for x in test_text:
        # sentence = "do you use credit cards?"

        sentence = x
        test = ""

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
            print(prob.item())
            for intent in intents['intents']:
                if tag == intent["tag"]:
                    print(f"{bot_name}: {random.choice(intent['responses'])}")
                    test = random.choice(intent['responses'])
        else:
            print(prob.item())
            print(f"{bot_name}: I do not understand...")
            test = "I do not understand..."

        num = str(prob.item()).replace(".", ",")
        writer.writerow((id_num,x,num,test))
        id_num = id_num + 1