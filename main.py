from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem

import ui_windows


if __name__ == "__main__":
    # show the window
    app = QApplication([])
    window = QDialog()
    ui = ui_windows.Ui_STAT()
    ui.setupUi(window)

    # ui.label.setText("Hello World")
    ui.label.adjustSize()

    window.show()
    app.exec()
