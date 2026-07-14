# widgets/popup_menu.py
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal, Qt
from pyDocs.MenuPanel import Ui_VerticalLayout as Ui_MenuPanel  # yes, Ui_VerticalLayout — see note below

class PopupMenu(QWidget, Ui_MenuPanel):
    navigate_requested = Signal(str)
    close_requested = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.CommandsButton.clicked.connect(lambda: self.navigate_requested.emit("controls"))
        self.AlarmsStatusButton.clicked.connect(lambda: self.navigate_requested.emit("alarm_status"))
        self.CloseButton.clicked.connect(lambda: self.close_requested.emit())