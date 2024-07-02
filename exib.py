# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exib.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(353, 372)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtSetor = QLabel(Form)
        self.txtSetor.setObjectName(u"txtSetor")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.txtSetor.setFont(font)
        self.txtSetor.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txtSetor)

        self.treeVisSetor = QTreeWidget(Form)
        self.treeVisSetor.setObjectName(u"treeVisSetor")

        self.verticalLayout.addWidget(self.treeVisSetor)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.txtSetor.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        ___qtreewidgetitem = self.treeVisSetor.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"CELA", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"NOME", None));
    # retranslateUi

