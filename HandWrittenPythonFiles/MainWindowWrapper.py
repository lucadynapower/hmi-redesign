# widgets/main_window.py
from PySide6.QtWidgets import QMainWindow
from pyDocs.MainWindow import Ui_MainWindow
from HandWrittenPythonFiles.AlarmStatusWrapper import AlarmStatusWidget
from HandWrittenPythonFiles.ControlsWidgetWrapper import ControlsWidget
from HandWrittenPythonFiles.MenuPanelWrapper import PopupMenu

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pages = {
            "alarm_status": AlarmStatusWidget(),
            "controls": ControlsWidget(),
        }
        for page in self.pages.values():
            self.pageStack.addWidget(page)

        self.popup_menu = PopupMenu(self.centralwidget)
        self.popup_menu.hide()

        self.MenuButton.clicked.connect(self.toggle_popup_menu)

        self.popup_menu.navigate_requested.connect(self.show_page)
        self.popup_menu.navigate_requested.connect(lambda _name: self.close_popup_menu())
        self.popup_menu.close_requested.connect(self.close_popup_menu)

        self.show_page("controls")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.popup_menu.isVisible():
            self._resize_popup_menu()

    def _resize_popup_menu(self):
        width = self.centralwidget.width() // 3
        height = self.centralwidget.height()
        self.popup_menu.setGeometry(0, 0, width, height)

    def show_page(self, name):
        self.pageStack.setCurrentWidget(self.pages[name])

    def toggle_popup_menu(self):
        self.popup_menu.hide() if self.popup_menu.isVisible() else self._open_popup_menu()

    def _open_popup_menu(self):
        self._resize_popup_menu()
        self.popup_menu.show()
        self.popup_menu.raise_()

    def close_popup_menu(self):
        self.popup_menu.hide()