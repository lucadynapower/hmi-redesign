# widgets/controls_widget.py
from PySide6.QtWidgets import QWidget
from pyDocs.ControlsWidget import Ui_Form as Ui_ControlsWidget

class ControlsWidget(QWidget, Ui_ControlsWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)