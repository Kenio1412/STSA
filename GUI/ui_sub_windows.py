# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_windows.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.Ensure = QPushButton(Form)
        self.Ensure.setObjectName(u"Ensure")
        self.Ensure.setGeometry(QRect(80, 250, 75, 24))
        self.Cancel = QPushButton(Form)
        self.Cancel.setObjectName(u"Cancel")
        self.Cancel.setGeometry(QRect(240, 250, 75, 24))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 71, 16))
        font = QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(70, 90, 81, 22))
        self.spinBox_2 = QSpinBox(Form)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(70, 130, 81, 22))
        self.key1_name = QLabel(Form)
        self.key1_name.setObjectName(u"key1_name")
        self.key1_name.setGeometry(QRect(40, 93, 54, 16))
        font1 = QFont()
        font1.setPointSize(12)
        self.key1_name.setFont(font1)
        self.key2_name = QLabel(Form)
        self.key2_name.setObjectName(u"key2_name")
        self.key2_name.setGeometry(QRect(40, 133, 54, 16))
        self.key2_name.setFont(font1)
        self.Encrypt = QRadioButton(Form)
        self.Encrypt.setObjectName(u"Encrypt")
        self.Encrypt.setGeometry(QRect(240, 90, 98, 20))
        self.Decrypt = QRadioButton(Form)
        self.Decrypt.setObjectName(u"Decrypt")
        self.Decrypt.setGeometry(QRect(240, 130, 98, 20))
        self.Playfair_key = QTextEdit(Form)
        self.Playfair_key.setObjectName(u"Playfair_key")
        self.Playfair_key.setGeometry(QRect(70, 90, 104, 71))
        self.From = QTextEdit(Form)
        self.From.setObjectName(u"From")
        self.From.setGeometry(QRect(80, 90, 101, 31))
        self.To = QTextEdit(Form)
        self.To.setObjectName(u"To")
        self.To.setGeometry(QRect(80, 130, 101, 31))
        self.Tips_text = QTextBrowser(Form)
        self.Tips_text.setObjectName(u"Tips_text")
        self.Tips_text.setGeometry(QRect(20, 10, 331, 241))
        self.Tips_text.raise_()
        self.Playfair_key.raise_()
        self.Ensure.raise_()
        self.Cancel.raise_()
        self.label.raise_()
        self.spinBox.raise_()
        self.spinBox_2.raise_()
        self.key1_name.raise_()
        self.key2_name.raise_()
        self.Encrypt.raise_()
        self.Decrypt.raise_()
        self.From.raise_()
        self.To.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Details", None))
        self.Ensure.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.Cancel.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5bc6\u94a5key\uff1a", None))
        self.key1_name.setText(QCoreApplication.translate("Form", u"a:", None))
        self.key2_name.setText(QCoreApplication.translate("Form", u"b:", None))
        self.Encrypt.setText(QCoreApplication.translate("Form", u"Encrypt", None))
        self.Decrypt.setText(QCoreApplication.translate("Form", u"Decrypt", None))
    # retranslateUi

