# test_popup_signals.py
import sys
from PySide6.QtWidgets import QApplication
from HandWrittenPythonFiles.MenuPanelWrapper import PopupMenu

app = QApplication(sys.argv)
window = PopupMenu()
window.navigate_requested.connect(lambda name: print(f"navigate_requested: {name}"))
window.close_requested.connect(lambda: print("close_requested"))
window.show()
sys.exit(app.exec())