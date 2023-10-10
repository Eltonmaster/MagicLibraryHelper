from PyQt6.QtWidgets import QMainWindow, QGridLayout, QWidget, QLabel, QListWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QSize, Qt
from gui.TextEdit import TextEdit
from gui.ListWidget import ListWidget
import requests, os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MLH")
        layout = QGridLayout()
        layout.setSpacing(15)
        text_edit = ListWidget()
        if os.path.exists("db.json"):
            text_edit.import_db("db.json")
        text_edit2 = TextEdit("Decklist-Stuff")
        card_image = QPixmap("./gui/placeholder.png")          # if not loaded from bytes can use QPixmap(_path_to_image_file_)
        #resp = requests.get("https://cards.scryfall.io/png/front/d/5/d5806e68-1054-458e-866d-1f2470f682b2.png?1696020224").content
        #card_image.loadFromData(resp)
        card_image_scaled = card_image.scaled(450, 450, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        lbl = QLabel(self)
        lbl.setPixmap(card_image_scaled)
        layout.addWidget(text_edit, 0, 0, 2, 1)
        layout.addWidget(lbl, 0, 1)
        layout.addWidget(text_edit2, 1, 1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)