from PyQt6.QtWidgets import QTextEdit


class TextEdit(QTextEdit):
    def __init__(self, title):
        super().__init__(title)
        self.setAcceptDrops(True)

    def dropEvent(self, e):
        path = e.mimeData().text()[8:]
        print(path)
        text = self.handle_file(path)
        self.setText(text)
        super().dropEvent(e)

    def handle_file(self, path_to_file):
        if path_to_file.endswith(".txt"):
            with open(path_to_file, "r") as f:
                return f.read()
        elif path_to_file.endswith(".csv"):
            # todo
            pass