import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QToolBar
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QIcon
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()

        # create a QWebEngineView widget and set it as the central widget
        self.view = QWebEngineView(self)
        self.setCentralWidget(self.view)

        # create a QLineEdit widget and set its style to match Safari's URL bar
        self.lineedit = QLineEdit(self)
        self.lineedit.setStyleSheet("""
            QLineEdit {
                border: none;
                background-color: #fafafa;
                font-size: 13pt;
                padding: 8px;
            }
            QLineEdit:focus {
                background-color: #ffffff;
                border: 1px solid #7d7d7d;
            }
        """)
        self.lineedit.returnPressed.connect(self.search)

        # create a QToolBar and add the QLineEdit widget to it
        self.toolbar = QToolBar(self)
        self.toolbar.addWidget(self.lineedit)
        self.toolbar.setMovable(False)

        # add the QToolBar to the main window
        self.addToolBar(self.toolbar)

        # set the initial URL
        self.lineedit.setText("https://www.google.com")
        self.view.load(QUrl("https://www.google.com"))

        # set the window flags to match the style of macOS window buttons
        self.setWindowFlag(Qt.CustomizeWindowHint, True)
        self.setWindowFlag(Qt.WindowTitleHint, True)
        self.setWindowFlag(Qt.WindowCloseButtonHint, True)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        self.setWindowTitle("")
        self.setWindowIcon(QIcon("path/to/icon.png"))
    def search(self):
        # get the search query from the QLineEdit widget
        query = self.lineedit.text()

        # create the search URL
        search_url = "https://www.google.com/search?q=" + query

        # load the search page
        self.view.load(QUrl(search_url))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.showMaximized()
    sys.exit(app.exec_())