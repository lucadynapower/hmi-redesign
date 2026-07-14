# test_controls.py
import sys
from PySide6.QtWidgets import QApplication
from HandWrittenPythonFiles.ControlsWidgetWrapper import ControlsWidget

app = QApplication(sys.argv)
window = ControlsWidget()
window.show()
sys.exit(app.exec())