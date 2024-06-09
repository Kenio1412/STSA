from PySide6.QtWidgets import QApplication
import sys

from MainForm import MainWindow

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
