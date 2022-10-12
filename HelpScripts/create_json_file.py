import json


def create_character_json():

    # new line 10
    # leerzeichen 32
    # loeschen 13
    # tab 9
    not_complete_json = []
    j_proto = {
        "tag": "delete",
        "patterns": [
            "delete",
            "löschen",
            "loeschen",
            "zurück"
        ],
        "responses": [
            "delete"
        ]
    }
    not_complete_json.append(j_proto)

    j_proto = {
        "tag": "stop",
        "patterns": [
            "stop",
            "beenden",
            "ende",
            "sicher",
            "save"
        ],
        "responses": [
            "stop"
        ]
    }
    not_complete_json.append(j_proto)


    run = 0
    for i in range(9, 10):
        key = chr(i)
        j_proto = {
            "tag": "tab",
            "patterns": [
                "tab",

            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1

    symbol_de = ["leertaste", "ausrufezeichen","Anführungszeichen","doppelkreuz","dollar",
                 "prozent", "und zeichen","apostroph", "runde öffnende Klammer", "runde schließende Klammer",
                 "Stern","plus", "komma", "minus", "punkt",
                 "schrägstrich"]

    symbol_en = ["space", "exclamation mark", "quotation mark", "double cross", "dollar",
                 "percent", "and sign", "apostrophe", "round opening bracket", "round closing bracket",
                 "asterisk", "plus", "comma", "minus", "period",
                 "slash"]
    symbol_de_2 = ["abstand", "rufezeichen", "", "Hashtag", "",
                 "prozent", "und", "", "runde Klammer links", "runde Klammer rechts",
                 "Multiplikation", "", "komma", "minus", "punkt",
                 "dividieren"]




    run = 0
    for i in range(32,48):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns":[
                str(symbol_de[run]),
                str(symbol_en[run]),
                str(symbol_de_2[run]),
                str(key)
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1

    symbol_de = ["null", "eins", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun"]
    symbol_en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    symbol_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    run = 0
    for i in range(48, 58):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns": [
                str(symbol_de[run]),
                str(symbol_en[run]),
                str(symbol_num[run])
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1

    symbol_de = ["Doppelpunkt", "Semikolon", "Kleiner als", "Gleichheitszeichen", "Größer als", "Fragezeichen", "at-Zeichen"]
    symbol_en = ["colon", "semicolon", "less than", "equal sign", "greater than", "question mark", "at sign"]

    run = 0
    for i in range(58, 65):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns": [
                str(symbol_de[run]),
                str(symbol_en[run]),
                str(key)
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1

    run = 0
    for i in range(65, 91):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns": [
                "Großbuchstabe "+str(key),
                "Capital letters "+str(key),
                str(key),
                "Groß " + str(key),
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1


    symbol_de = ["Linke eckige Klammer", "Umgekehrter Schrägstrich Backslash", "Rechte eckige Klammer", "Zirkumflex", "Unterstrich", "Gravis"]
    symbol_de_2 = ["", "Backslash", "", "",
                 "", "Backtick"]
    symbol_en = ["Left square bracket", "Reverse slash backslash", "Right square bracket", "Circumflex", "Underscore", "Gravis"]

    run = 0
    for i in range(91, 96):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns": [
                str(symbol_de[run]),
                str(symbol_de_2[run]),
                str(symbol_en[run]),
                str(key)
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1

    run = 0
    for i in range(96, 123):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns": [
                "Kleinbuchstaben " + str(key),
                "Klein " + str(key),
                "Lower case letters " + str(key),
                str(key)
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1



    symbol_de = ["Linke geschweifte Klammer", "Senkrechter Strich Pipe", "Rechte geschweifte Klammer", "Tilde"]
    symbol_en = ["Left Curly Bracket", "Vertical Stroke Pipe", "Right Curly Bracket", "Tilde"]

    run = 0
    for i in range(123, 127):
        key = chr(i)
        j_proto = {
            "tag": str(key),
            "patterns": [
                str(symbol_de[run]),
                str(symbol_en[run]),
                str(key)
            ],
            "responses": [
                chr(i)
            ]
        }
        not_complete_json.append(j_proto)
        run += 1

    # print(not_complete_json)

    json_output = {"intents": not_complete_json}


    with open('../deepLearning/jsonFiles/ascii.json', 'w') as f:
        json.dump(json_output, f, indent=2)
        print("New json file is created from data.json file")


if __name__ == '__main__':
    create_character_json()