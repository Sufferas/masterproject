
import json

def create_character_json():

    # new line 10
    # leerzeichen 32
    # loeschen 13
    # tab 9

    symbol_de = ["leertaste", "ausrufezeichen","Anführungszeichen","doppelkreuz","dollar",
                 "prozent", "und zeichen","apostroph", "runde öffnende Klammer", "runde schließende Klammer",
                 "Stern","plus", "komma", "minus", "punkt",
                 "schrägstrich"]

    symbol_en = ["space", "exclamation mark", "quotation mark", "double cross", "dollar",
                 "percent", "and sign", "apostrophe", "round opening bracket", "round closing bracket",
                 "asterisk", "plus", "comma", "minus", "period",
                 "slash"]

    not_complete_json =[]

    run = 0
    for i in range(32,48):
        key = chr(i)
        print(key)
        j_proto = {
            "tag": str(key),
            "patterns":[
                str(symbol_de[run]),
                str(symbol_en[run])
            ],
            "responses": [
                str(key)
            ]
        }
        not_complete_json.append(j_proto)


        run += 1

    print(not_complete_json)

    not_coplite_json = [
    {
      "tag": "yes",
      "patterns": [
        "yes",
        "yes please",
        "ja",
        "yes sure",
        "sure yes",
        "y"
      ],
      "responses": [
        "YES"
      ]
    }
  ]


if __name__ == '__main__':
    create_character_json()