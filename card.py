import json
import re


class Card:
    card_name = ""
    extension_code = ""
    collector_number = ""
    number = ""

    def __init__(self, number, card_name, extension_code="", collector_number=""):
        self.card_name = card_name
        self.extension_code = extension_code
        self.collector_number = collector_number
        self.number = number

    @classmethod
    def from_string(cls, import_string):
        try:
            match = re.search(r'^(\d+) (.+) \((.+)\) (\d+)', import_string)
            if match:
                number = match.group(1)
                card_name = match.group(2)
                extension_code = match.group(3)
                collector_number = match.group(4)
            else:
                match = re.search(r'^(\d+) (.+)$', import_string)
                number = match.group(1)
                card_name = match.group(2)
                extension_code = "---"
                collector_number = "---"
            return cls(number, card_name, extension_code, collector_number)
        except AttributeError as att_ex:
            print("\n" + import_string + "\n")
            print(att_ex)

    @classmethod
    def from_dict(cls, import_cls):
        return cls(import_cls["number"], import_cls["card_name"], import_cls["extension_code"], import_cls["collector_number"])

    def to_dict(self):
        return {
            "card_name": self.card_name,
            "extension_code": self.extension_code,
            "collector_number": self.collector_number,
            "number": self.number
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def equals(self, x):
        return self.card_name == x.card_name #and self.extension_code == x.extension_code and self.collector_number == x.collector_number

    def __str__(self):
        if self.extension_code != "":
            return f"Name: {self.card_name}\nExtension Code: {self.extension_code}\nCollector Number: {self.collector_number}\nNumber: {self.number}\n"
        return f"Name: {self.card_name}\nNumber: {self.number}\n"

    def to_export_string(self):
        if self.extension_code != "":
            return f"{self.number} {self.card_name} ({self.extension_code}) {self.collector_number}\n"
        return f"{self.number} {self.card_name}\n"

    def to_stripped_export_string(self):
        return f"{self.number} {self.card_name}\n"


def sort_cards(list_of_cards):
    if isinstance(list_of_cards[0], str):
        print("Sort list of strings")
        return sorted(list_of_cards, key=lambda x:x[x.find(" "):])
    if isinstance(list_of_cards[0], Card):
        print("Sort list of Cards")
        return sorted(list_of_cards, key=lambda x:x.card_name)
