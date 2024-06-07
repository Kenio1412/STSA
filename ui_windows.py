# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windows.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_STAT(object):
    def setupUi(self, STAT):
        if not STAT.objectName():
            STAT.setObjectName(u"STAT")
        STAT.resize(400, 300)
        self.buttonBox = QDialogButtonBox(STAT)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setEnabled(True)
        self.buttonBox.setGeometry(QRect(30, 250, 341, 32))
        self.buttonBox.setMouseTracking(False)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(STAT)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 40, 54, 16))
        self.pushButton = QPushButton(STAT)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(270, 170, 75, 24))
        self.textEdit = QTextEdit(STAT)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 80, 161, 121))

        self.retranslateUi(STAT)
        self.buttonBox.accepted.connect(STAT.accept)
        self.buttonBox.rejected.connect(STAT.reject)
        self.pushButton.clicked.connect(self.pushButton_clicked)

        QMetaObject.connectSlotsByName(STAT)

    def pushButton_clicked(self):
        s = self.textEdit.toPlainText()
        self.textEdit.clear()
        self.textEdit.append('You entered: ' + s + '\n')
        self.label.setText('You entered: ' + s)
        self.label.adjustSize()
    # setupUi

    def retranslateUi(self, STAT):
        STAT.setWindowTitle(QCoreApplication.translate("STAT", u"STAT", None))
        self.label.setText(QCoreApplication.translate("STAT", u"TextLabel", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("STAT", u"<html><head/><body><p>\uff1f\uff1f\uff1f\uff1f\uff1f\uff1f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton.setWhatsThis(QCoreApplication.translate("STAT", u"<html><head/><body><p>123</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.pushButton.setText(QCoreApplication.translate("STAT", u"PushButton", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("STAT", u"\u8bf7\u8f93\u5165\u5b57\u7b26\u4e32", None))
    # retranslateUi

