# test_alarm_status.py
import sys
from PySide6.QtWidgets import QApplication
from HandWrittenPythonFiles.AlarmStatusWrapper import AlarmStatusWidget

app = QApplication(sys.argv)
window = AlarmStatusWidget()
window.show()
sys.exit(app.exec())