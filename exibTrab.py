# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'exibTrab.ui'
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

class Ui_Form_Trab(object):
    def setupUiExibTrab(self, formExibTrab):
        if not formExibTrab.objectName():
            formExibTrab.setObjectName(u"formExibTrab")
        formExibTrab.resize(255, 239)
        self.verticalLayout = QVBoxLayout(formExibTrab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txtSetor = QLabel(formExibTrab)
        self.txtSetor.setObjectName(u"txtSetor")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.txtSetor.setFont(font)
        self.txtSetor.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.txtSetor.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txtSetor)

        self.treeVisSetor = QTreeWidget(formExibTrab)
        self.treeVisSetor.setObjectName(u"treeVisSetor")

        self.verticalLayout.addWidget(self.treeVisSetor)


        self.retranslateUi(formExibTrab)

        QMetaObject.connectSlotsByName(formExibTrab)
    # setupUi

    def retranslateUi(self, formExibTrab):
        formExibTrab.setWindowTitle(QCoreApplication.translate("formExibTrab", u"Form", None))
        self.txtSetor.setText(QCoreApplication.translate("formExibTrab", u"SETOR", None))
        ___qtreewidgetitem = self.treeVisSetor.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("formExibTrab", u"CELA", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("formExibTrab", u"NOME", None));
    # retranslateUi

