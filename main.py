from card import Card
import json
import os
import re
import argparse
import pyperclip
import sys


FILE_HANDLE = ""

def add_cards_to_db(card_db):
    new_cards = load_new_cards_from_txt(card_db)
    if len(new_cards) > 0:
        store_card_db(card_db+new_cards)
    print(f"{len(new_cards)} new cards added to db")


def search_in_db(card_obj, card_db):    # returns entry if already in db else None
    for entry in card_db:
        if entry.equals(card_obj):
            return entry
    return None


def lookup_decklist(card_db):
    decklist = load_new_cards_from_txt(card_db)
    for entry in decklist:
        if search_in_db(entry, card_db):
            decklist.remove(entry)
    if len(decklist) == 0:
        print("You own all the cards from the decklist")
        return
    print("Cards Needed:\n")
    for entry in decklist:
        print(entry)
    print(f"In total {len(decklist)} card(s) are needed")
    while True:
        export = input("Export needed cards into clipboard? (y|n): ")
        if export.lower() == "y":
            to_clip = ""
            for entry in decklist:
                to_clip += entry.to_export_string()
            pyperclip.copy(to_clip)
            print("Done")
            return
        if export.lower() == "n":
            return

    
def load_card_db():
    if not os.path.exists("db.json") or os.stat("db.json").st_size == 0:
        return []
    with open("db.json", "r") as f:
        dat = json.load(f)
    card_db = []
    for entry in dat:
        card_db.append(Card(entry["number"], entry["card_name"], entry["extension_code"], entry["collector_number"]))
    return card_db


def load_cards_from_txt():
    if not os.path.exists("cards.txt"):
        print("Missing 'cards.txt' file in root directory")
    temp_db = []
    with open(FILE_HANDLE, "r") as f:
        for line in f:
            try:
                match = re.search(r'^(\d+) (.+) \((.+)\) (\d+)', line)
                if match:
                    temp_number = match.group(1)
                    temp_name = match.group(2)
                    temp_extension = match.group(3)
                    temp_collector = match.group(4)
                    temp_card = Card(temp_number, temp_name, temp_extension, temp_collector)
                else:
                    match = re.search(r'^(\d+) (.+)$', line)
                    temp_number = match.group(1)
                    temp_name = match.group(2)
                    temp_card = Card(temp_number, temp_name)
            except AttributeError as att_ex:
                print("\n"+line+"\n")
                print(att_ex)
                sys.exit()
            temp_db.append(temp_card)
    return temp_db


def load_new_cards_from_txt(card_db):
    cards = load_cards_from_txt()
    new_cards = []
    for entry in cards:
        if not search_in_db(entry, card_db):
            new_cards.append(entry)
    return new_cards


def store_card_db(card_db):
    with open("db.json", "w") as f:
        f.write(json.dumps([x.to_dict() for x in card_db], indent=4))


def copy_stripped_list():
    cards = load_cards_from_txt()
    to_clip = ""
    for entry in cards:
        to_clip += entry.to_stripped_export_string()
    pyperclip.copy(to_clip)
    print("Added stripped list to clipboard")


def setup_argparse():
    parser = argparse.ArgumentParser(
        prog="MagicLibraryHelper",
        description="MLH is a tool to quickly look up needed cards for a decklist."
    )
    parser.add_argument('filename')
    parser.add_argument(
        '-a',
        '--add_to_db',
        action="store_true",
        help="Reads the content of the .txt file and adds all the missing cards into db"
    )
    parser.add_argument(
        '-d',
        '--decklist_lookup',
        action="store_true",
        help="Reads the content of the .txt file and prints out a list of all the cards missing from db"
    )
    parser.add_argument(
        '-s',
        '--strip',
        action="store_true",
        help="Reads the content of the card list contained in the .txt file and copys the the version stripped of extension code and collectors number to the clipboard"
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = setup_argparse()
    FILE_HANDLE = args.filename
    card_db = load_card_db()
    if args.add_to_db:
        add_cards_to_db(card_db)
    elif args.decklist_lookup:
        lookup_decklist(card_db)
    elif args.strip:
        copy_stripped_list()
    print("\nThanks for using MLH :)")
