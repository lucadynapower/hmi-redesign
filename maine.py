from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtUiTools import QUiLoader
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        
        loader = QUiLoader()
        self.ui = loader.load("mainui.ui",self)
        self.ui.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    app.exec()