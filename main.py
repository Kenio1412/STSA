from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem
from PySide6.QtCore import Signal, Slot
import sys

from MainForm import MainWindow
import ui_windows


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
