import PyQt6.QtWidgets
from PyQt6.QtWidgets import QListWidget
from PyQt6 import QtWidgets
from PyQt6 import QtCore
from card import sort_cards, Card
import json


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(ListWidget, self).__init__(parent)
        self.setIconSize(QtCore.QSize(124, 124))
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)

    def dragEnterEvent(self, event):    # Needs to be implemented for drop Icon to display right mode (not crossed out)
        if event.mimeData().hasUrls():
            event.accept()
        else:
            super(ListWidget, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):     # Needs to be implemented for drop Icon to display right mode (not crossed out)
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
        else:
            super(ListWidget, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.DropAction.CopyAction)
            event.accept()
            card_list = self.handle_file(event.mimeData().text()[8:])   # Strip the first chars of file:///C:/XX/YY/...
        else:
            super(ListWidget, self).dropEvent(event)

    def handle_file(self, path_to_file):    # Returns list of card objects alphabetically sorted
        print(f"[Drop Event] Path: {path_to_file}")
        if path_to_file.endswith(".txt"):
            with open(path_to_file, "r", encoding="utf-8") as f:
                f_content = f.read()
                for entry in sort_cards([x for x in f_content.strip().split("\n")]):

                    self.addItem(entry.strip())
        elif path_to_file.endswith(".csv"):
            # todo
            pass

    def import_db(self, path_to_db):
        with open(path_to_db, "r") as f:
            temp_db = json.load(f)
            db = [Card(x["number"], x["card_name"], x["extension_code"], x["collector_number"]) for x in temp_db]
            db = sort_cards(db)
            for entry in db:
                self.addItem(f"{entry.number} {entry.card_name} {entry.extension_code} {entry.collector_number}")

