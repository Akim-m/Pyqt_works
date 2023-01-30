import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App")
        self.button=QPushButton("press button")
        self.button.clicked.connect(self.button_was_clicked)
        self.windowTitleChanged.connect(self.title_change)

        self.setCentralWidget(self.button)

    def button_was_clicked(self):
        print("clicked")
        new_window_title=choice(window_titles)
        print("Setting title: %s" %new_window_title)
        self.setWindowTitle(new_window_title)






app= QApplication(sys.argv)

window=MainWindow()
window.show()

app.exec()
