import json


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
    