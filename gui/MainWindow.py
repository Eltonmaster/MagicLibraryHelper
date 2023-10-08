from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QSize
from gui.TextEdit import TextEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drag And Drop Test")
        self.setFixedSize(QSize(300,400))
        text_edit = TextEdit("Test")
        self.setCentralWidget(text_edit)