# widgets/alarm_status_widget.py
from PySide6.QtWidgets import QWidget
from pyDocs.AlarmStatus import Ui_MainLayout as Ui_AlarmStatus

class AlarmStatusWidget(QWidget, Ui_AlarmStatus):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)