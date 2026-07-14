# test_popup.py
import sys
from PySide6.QtWidgets import QApplication
from HandWrittenPythonFiles.MenuPanelWrapper import PopupMenu

app = QApplication(sys.argv)
window = PopupMenu()
window.show()
sys.exit(app.exec())