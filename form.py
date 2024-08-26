# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QDateTimeEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableView,
    QToolButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(780, 923)
        self.verticalLayout_9 = QVBoxLayout(Widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(70000, 700000))
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabExib = QWidget()
        self.tabExib.setObjectName(u"tabExib")
        self.gridLayout_4 = QGridLayout(self.tabExib)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frameExib = QFrame(self.tabExib)
        self.frameExib.setObjectName(u"frameExib")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameExib.sizePolicy().hasHeightForWidth())
        self.frameExib.setSizePolicy(sizePolicy)
        self.frameExib.setFrameShape(QFrame.StyledPanel)
        self.frameExib.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frameExib)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.frame_setor_7 = QFrame(self.frameExib)
        self.frame_setor_7.setObjectName(u"frame_setor_7")
        self.frame_setor_7.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(250)
        sizePolicy1.setVerticalStretch(250)
        sizePolicy1.setHeightForWidth(self.frame_setor_7.sizePolicy().hasHeightForWidth())
        self.frame_setor_7.setSizePolicy(sizePolicy1)
        self.frame_setor_7.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_setor_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_setor_7 = QLabel(self.frame_setor_7)
        self.label_setor_7.setObjectName(u"label_setor_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(250)
        sizePolicy2.setVerticalStretch(25)
        sizePolicy2.setHeightForWidth(self.label_setor_7.sizePolicy().hasHeightForWidth())
        self.label_setor_7.setSizePolicy(sizePolicy2)
        self.label_setor_7.setMaximumSize(QSize(16777215, 20))
        self.label_setor_7.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_setor_7)

        self.tw_setor_7 = QTreeWidget(self.frame_setor_7)
        self.tw_setor_7.setObjectName(u"tw_setor_7")

        self.verticalLayout_19.addWidget(self.tw_setor_7)


        self.gridLayout_6.addWidget(self.frame_setor_7, 2, 0, 1, 1)

        self.frame_setor_3 = QFrame(self.frameExib)
        self.frame_setor_3.setObjectName(u"frame_setor_3")
        self.frame_setor_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_3.sizePolicy().hasHeightForWidth())
        self.frame_setor_3.setSizePolicy(sizePolicy1)
        self.frame_setor_3.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_setor_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_setor_3 = QLabel(self.frame_setor_3)
        self.label_setor_3.setObjectName(u"label_setor_3")
        sizePolicy2.setHeightForWidth(self.label_setor_3.sizePolicy().hasHeightForWidth())
        self.label_setor_3.setSizePolicy(sizePolicy2)
        self.label_setor_3.setMaximumSize(QSize(16777215, 20))
        self.label_setor_3.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_setor_3)

        self.tw_setor_3 = QTreeWidget(self.frame_setor_3)
        self.tw_setor_3.setObjectName(u"tw_setor_3")

        self.verticalLayout_15.addWidget(self.tw_setor_3)


        self.gridLayout_6.addWidget(self.frame_setor_3, 0, 2, 1, 1)

        self.frame_setor_10 = QFrame(self.frameExib)
        self.frame_setor_10.setObjectName(u"frame_setor_10")
        self.frame_setor_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_10.sizePolicy().hasHeightForWidth())
        self.frame_setor_10.setSizePolicy(sizePolicy1)
        self.frame_setor_10.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_setor_10)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_setor_10 = QLabel(self.frame_setor_10)
        self.label_setor_10.setObjectName(u"label_setor_10")
        sizePolicy2.setHeightForWidth(self.label_setor_10.sizePolicy().hasHeightForWidth())
        self.label_setor_10.setSizePolicy(sizePolicy2)
        self.label_setor_10.setMaximumSize(QSize(16777215, 20))
        self.label_setor_10.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_setor_10)

        self.tw_setor_10 = QTreeWidget(self.frame_setor_10)
        self.tw_setor_10.setObjectName(u"tw_setor_10")

        self.verticalLayout_22.addWidget(self.tw_setor_10)


        self.gridLayout_6.addWidget(self.frame_setor_10, 3, 0, 1, 1)

        self.frame_setor_11 = QFrame(self.frameExib)
        self.frame_setor_11.setObjectName(u"frame_setor_11")
        self.frame_setor_11.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_11.sizePolicy().hasHeightForWidth())
        self.frame_setor_11.setSizePolicy(sizePolicy1)
        self.frame_setor_11.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_setor_11)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_setor_11 = QLabel(self.frame_setor_11)
        self.label_setor_11.setObjectName(u"label_setor_11")
        sizePolicy2.setHeightForWidth(self.label_setor_11.sizePolicy().hasHeightForWidth())
        self.label_setor_11.setSizePolicy(sizePolicy2)
        self.label_setor_11.setMaximumSize(QSize(16777215, 20))
        self.label_setor_11.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_setor_11)

        self.tw_setor_11 = QTreeWidget(self.frame_setor_11)
        self.tw_setor_11.setObjectName(u"tw_setor_11")

        self.verticalLayout_23.addWidget(self.tw_setor_11)


        self.gridLayout_6.addWidget(self.frame_setor_11, 3, 1, 1, 1)

        self.frame_setor_4 = QFrame(self.frameExib)
        self.frame_setor_4.setObjectName(u"frame_setor_4")
        self.frame_setor_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_4.sizePolicy().hasHeightForWidth())
        self.frame_setor_4.setSizePolicy(sizePolicy1)
        self.frame_setor_4.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_setor_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_setor_4 = QLabel(self.frame_setor_4)
        self.label_setor_4.setObjectName(u"label_setor_4")
        sizePolicy2.setHeightForWidth(self.label_setor_4.sizePolicy().hasHeightForWidth())
        self.label_setor_4.setSizePolicy(sizePolicy2)
        self.label_setor_4.setMaximumSize(QSize(16777215, 20))
        self.label_setor_4.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_setor_4)

        self.tw_setor_4 = QTreeWidget(self.frame_setor_4)
        self.tw_setor_4.setObjectName(u"tw_setor_4")

        self.verticalLayout_16.addWidget(self.tw_setor_4)


        self.gridLayout_6.addWidget(self.frame_setor_4, 1, 0, 1, 1)

        self.frame_setor_1 = QFrame(self.frameExib)
        self.frame_setor_1.setObjectName(u"frame_setor_1")
        self.frame_setor_1.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_1.sizePolicy().hasHeightForWidth())
        self.frame_setor_1.setSizePolicy(sizePolicy1)
        self.frame_setor_1.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_setor_1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_setor_1 = QLabel(self.frame_setor_1)
        self.label_setor_1.setObjectName(u"label_setor_1")
        sizePolicy2.setHeightForWidth(self.label_setor_1.sizePolicy().hasHeightForWidth())
        self.label_setor_1.setSizePolicy(sizePolicy2)
        self.label_setor_1.setMaximumSize(QSize(16777215, 20))
        self.label_setor_1.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_setor_1)

        self.tw_setor_1 = QTreeWidget(self.frame_setor_1)
        self.tw_setor_1.setObjectName(u"tw_setor_1")

        self.verticalLayout_13.addWidget(self.tw_setor_1)


        self.gridLayout_6.addWidget(self.frame_setor_1, 0, 0, 1, 1)

        self.frame_setor_20 = QFrame(self.frameExib)
        self.frame_setor_20.setObjectName(u"frame_setor_20")
        self.frame_setor_20.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_20.sizePolicy().hasHeightForWidth())
        self.frame_setor_20.setSizePolicy(sizePolicy1)
        self.frame_setor_20.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_setor_20)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_setor_20 = QLabel(self.frame_setor_20)
        self.label_setor_20.setObjectName(u"label_setor_20")
        sizePolicy2.setHeightForWidth(self.label_setor_20.sizePolicy().hasHeightForWidth())
        self.label_setor_20.setSizePolicy(sizePolicy2)
        self.label_setor_20.setMaximumSize(QSize(16777215, 20))
        self.label_setor_20.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_setor_20)

        self.tw_setor_20 = QTreeWidget(self.frame_setor_20)
        self.tw_setor_20.setObjectName(u"tw_setor_20")

        self.verticalLayout_32.addWidget(self.tw_setor_20)


        self.gridLayout_6.addWidget(self.frame_setor_20, 7, 1, 1, 1)

        self.frame_setor_14 = QFrame(self.frameExib)
        self.frame_setor_14.setObjectName(u"frame_setor_14")
        self.frame_setor_14.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_14.sizePolicy().hasHeightForWidth())
        self.frame_setor_14.setSizePolicy(sizePolicy1)
        self.frame_setor_14.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_setor_14)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_setor_14 = QLabel(self.frame_setor_14)
        self.label_setor_14.setObjectName(u"label_setor_14")
        sizePolicy2.setHeightForWidth(self.label_setor_14.sizePolicy().hasHeightForWidth())
        self.label_setor_14.setSizePolicy(sizePolicy2)
        self.label_setor_14.setMaximumSize(QSize(16777215, 20))
        self.label_setor_14.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_setor_14)

        self.tw_setor_14 = QTreeWidget(self.frame_setor_14)
        self.tw_setor_14.setObjectName(u"tw_setor_14")

        self.verticalLayout_26.addWidget(self.tw_setor_14)


        self.gridLayout_6.addWidget(self.frame_setor_14, 5, 1, 1, 1)

        self.frame_setor_6 = QFrame(self.frameExib)
        self.frame_setor_6.setObjectName(u"frame_setor_6")
        self.frame_setor_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_6.sizePolicy().hasHeightForWidth())
        self.frame_setor_6.setSizePolicy(sizePolicy1)
        self.frame_setor_6.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_setor_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_setor_6 = QLabel(self.frame_setor_6)
        self.label_setor_6.setObjectName(u"label_setor_6")
        sizePolicy2.setHeightForWidth(self.label_setor_6.sizePolicy().hasHeightForWidth())
        self.label_setor_6.setSizePolicy(sizePolicy2)
        self.label_setor_6.setMaximumSize(QSize(16777215, 20))
        self.label_setor_6.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_setor_6)

        self.tw_setor_6 = QTreeWidget(self.frame_setor_6)
        self.tw_setor_6.setObjectName(u"tw_setor_6")

        self.verticalLayout_18.addWidget(self.tw_setor_6)


        self.gridLayout_6.addWidget(self.frame_setor_6, 1, 2, 1, 1)

        self.frame_setor_13 = QFrame(self.frameExib)
        self.frame_setor_13.setObjectName(u"frame_setor_13")
        self.frame_setor_13.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_13.sizePolicy().hasHeightForWidth())
        self.frame_setor_13.setSizePolicy(sizePolicy1)
        self.frame_setor_13.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_setor_13)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_setor_13 = QLabel(self.frame_setor_13)
        self.label_setor_13.setObjectName(u"label_setor_13")
        sizePolicy2.setHeightForWidth(self.label_setor_13.sizePolicy().hasHeightForWidth())
        self.label_setor_13.setSizePolicy(sizePolicy2)
        self.label_setor_13.setMaximumSize(QSize(16777215, 20))
        self.label_setor_13.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_25.addWidget(self.label_setor_13)

        self.tw_setor_13 = QTreeWidget(self.frame_setor_13)
        self.tw_setor_13.setObjectName(u"tw_setor_13")

        self.verticalLayout_25.addWidget(self.tw_setor_13)


        self.gridLayout_6.addWidget(self.frame_setor_13, 5, 0, 1, 1)

        self.frame_setor_9 = QFrame(self.frameExib)
        self.frame_setor_9.setObjectName(u"frame_setor_9")
        self.frame_setor_9.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_9.sizePolicy().hasHeightForWidth())
        self.frame_setor_9.setSizePolicy(sizePolicy1)
        self.frame_setor_9.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_setor_9)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_setor_9 = QLabel(self.frame_setor_9)
        self.label_setor_9.setObjectName(u"label_setor_9")
        sizePolicy2.setHeightForWidth(self.label_setor_9.sizePolicy().hasHeightForWidth())
        self.label_setor_9.setSizePolicy(sizePolicy2)
        self.label_setor_9.setMaximumSize(QSize(16777215, 20))
        self.label_setor_9.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_setor_9)

        self.tw_setor_9 = QTreeWidget(self.frame_setor_9)
        self.tw_setor_9.setObjectName(u"tw_setor_9")

        self.verticalLayout_21.addWidget(self.tw_setor_9)


        self.gridLayout_6.addWidget(self.frame_setor_9, 2, 2, 1, 1)

        self.frame_setor_8 = QFrame(self.frameExib)
        self.frame_setor_8.setObjectName(u"frame_setor_8")
        self.frame_setor_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_8.sizePolicy().hasHeightForWidth())
        self.frame_setor_8.setSizePolicy(sizePolicy1)
        self.frame_setor_8.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_setor_8)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_setor_8 = QLabel(self.frame_setor_8)
        self.label_setor_8.setObjectName(u"label_setor_8")
        sizePolicy2.setHeightForWidth(self.label_setor_8.sizePolicy().hasHeightForWidth())
        self.label_setor_8.setSizePolicy(sizePolicy2)
        self.label_setor_8.setMaximumSize(QSize(16777215, 20))
        self.label_setor_8.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_setor_8)

        self.tw_setor_8 = QTreeWidget(self.frame_setor_8)
        self.tw_setor_8.setObjectName(u"tw_setor_8")

        self.verticalLayout_20.addWidget(self.tw_setor_8)


        self.gridLayout_6.addWidget(self.frame_setor_8, 2, 1, 1, 1)

        self.frame_setor_5 = QFrame(self.frameExib)
        self.frame_setor_5.setObjectName(u"frame_setor_5")
        self.frame_setor_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_5.sizePolicy().hasHeightForWidth())
        self.frame_setor_5.setSizePolicy(sizePolicy1)
        self.frame_setor_5.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_setor_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_setor_5 = QLabel(self.frame_setor_5)
        self.label_setor_5.setObjectName(u"label_setor_5")
        sizePolicy2.setHeightForWidth(self.label_setor_5.sizePolicy().hasHeightForWidth())
        self.label_setor_5.setSizePolicy(sizePolicy2)
        self.label_setor_5.setMaximumSize(QSize(16777215, 20))
        self.label_setor_5.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_setor_5)

        self.tw_setor_5 = QTreeWidget(self.frame_setor_5)
        self.tw_setor_5.setObjectName(u"tw_setor_5")

        self.verticalLayout_17.addWidget(self.tw_setor_5)


        self.gridLayout_6.addWidget(self.frame_setor_5, 1, 1, 1, 1)

        self.frame_setor_12 = QFrame(self.frameExib)
        self.frame_setor_12.setObjectName(u"frame_setor_12")
        self.frame_setor_12.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_12.sizePolicy().hasHeightForWidth())
        self.frame_setor_12.setSizePolicy(sizePolicy1)
        self.frame_setor_12.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_setor_12)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_setor_12 = QLabel(self.frame_setor_12)
        self.label_setor_12.setObjectName(u"label_setor_12")
        sizePolicy2.setHeightForWidth(self.label_setor_12.sizePolicy().hasHeightForWidth())
        self.label_setor_12.setSizePolicy(sizePolicy2)
        self.label_setor_12.setMaximumSize(QSize(16777215, 20))
        self.label_setor_12.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.label_setor_12)

        self.tw_setor_12 = QTreeWidget(self.frame_setor_12)
        self.tw_setor_12.setObjectName(u"tw_setor_12")

        self.verticalLayout_24.addWidget(self.tw_setor_12)


        self.gridLayout_6.addWidget(self.frame_setor_12, 3, 2, 1, 1)

        self.frame_setor_2 = QFrame(self.frameExib)
        self.frame_setor_2.setObjectName(u"frame_setor_2")
        self.frame_setor_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_2.sizePolicy().hasHeightForWidth())
        self.frame_setor_2.setSizePolicy(sizePolicy1)
        self.frame_setor_2.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_setor_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_setor_2 = QLabel(self.frame_setor_2)
        self.label_setor_2.setObjectName(u"label_setor_2")
        sizePolicy2.setHeightForWidth(self.label_setor_2.sizePolicy().hasHeightForWidth())
        self.label_setor_2.setSizePolicy(sizePolicy2)
        self.label_setor_2.setMaximumSize(QSize(16777215, 20))
        self.label_setor_2.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_setor_2)

        self.tw_setor_2 = QTreeWidget(self.frame_setor_2)
        self.tw_setor_2.setObjectName(u"tw_setor_2")

        self.verticalLayout_14.addWidget(self.tw_setor_2)


        self.gridLayout_6.addWidget(self.frame_setor_2, 0, 1, 1, 1)

        self.frame_setor_15 = QFrame(self.frameExib)
        self.frame_setor_15.setObjectName(u"frame_setor_15")
        self.frame_setor_15.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_15.sizePolicy().hasHeightForWidth())
        self.frame_setor_15.setSizePolicy(sizePolicy1)
        self.frame_setor_15.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_setor_15)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_setor_15 = QLabel(self.frame_setor_15)
        self.label_setor_15.setObjectName(u"label_setor_15")
        sizePolicy2.setHeightForWidth(self.label_setor_15.sizePolicy().hasHeightForWidth())
        self.label_setor_15.setSizePolicy(sizePolicy2)
        self.label_setor_15.setMaximumSize(QSize(16777215, 20))
        self.label_setor_15.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_setor_15)

        self.tw_setor_15 = QTreeWidget(self.frame_setor_15)
        self.tw_setor_15.setObjectName(u"tw_setor_15")

        self.verticalLayout_27.addWidget(self.tw_setor_15)


        self.gridLayout_6.addWidget(self.frame_setor_15, 5, 2, 1, 1)

        self.frame_setor_16 = QFrame(self.frameExib)
        self.frame_setor_16.setObjectName(u"frame_setor_16")
        self.frame_setor_16.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_16.sizePolicy().hasHeightForWidth())
        self.frame_setor_16.setSizePolicy(sizePolicy1)
        self.frame_setor_16.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_setor_16)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_setor_16 = QLabel(self.frame_setor_16)
        self.label_setor_16.setObjectName(u"label_setor_16")
        sizePolicy2.setHeightForWidth(self.label_setor_16.sizePolicy().hasHeightForWidth())
        self.label_setor_16.setSizePolicy(sizePolicy2)
        self.label_setor_16.setMaximumSize(QSize(16777215, 20))
        self.label_setor_16.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_setor_16)

        self.tw_setor_16 = QTreeWidget(self.frame_setor_16)
        self.tw_setor_16.setObjectName(u"tw_setor_16")

        self.verticalLayout_28.addWidget(self.tw_setor_16)


        self.gridLayout_6.addWidget(self.frame_setor_16, 6, 0, 1, 1)

        self.frame_setor_17 = QFrame(self.frameExib)
        self.frame_setor_17.setObjectName(u"frame_setor_17")
        self.frame_setor_17.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_17.sizePolicy().hasHeightForWidth())
        self.frame_setor_17.setSizePolicy(sizePolicy1)
        self.frame_setor_17.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_setor_17)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_setor_17 = QLabel(self.frame_setor_17)
        self.label_setor_17.setObjectName(u"label_setor_17")
        sizePolicy2.setHeightForWidth(self.label_setor_17.sizePolicy().hasHeightForWidth())
        self.label_setor_17.setSizePolicy(sizePolicy2)
        self.label_setor_17.setMaximumSize(QSize(16777215, 20))
        self.label_setor_17.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.label_setor_17)

        self.tw_setor_17 = QTreeWidget(self.frame_setor_17)
        self.tw_setor_17.setObjectName(u"tw_setor_17")

        self.verticalLayout_29.addWidget(self.tw_setor_17)


        self.gridLayout_6.addWidget(self.frame_setor_17, 6, 1, 1, 1)

        self.frame_setor_18 = QFrame(self.frameExib)
        self.frame_setor_18.setObjectName(u"frame_setor_18")
        self.frame_setor_18.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_18.sizePolicy().hasHeightForWidth())
        self.frame_setor_18.setSizePolicy(sizePolicy1)
        self.frame_setor_18.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_setor_18)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_setor_18 = QLabel(self.frame_setor_18)
        self.label_setor_18.setObjectName(u"label_setor_18")
        sizePolicy2.setHeightForWidth(self.label_setor_18.sizePolicy().hasHeightForWidth())
        self.label_setor_18.setSizePolicy(sizePolicy2)
        self.label_setor_18.setMaximumSize(QSize(16777215, 20))
        self.label_setor_18.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_setor_18)

        self.tw_setor_18 = QTreeWidget(self.frame_setor_18)
        self.tw_setor_18.setObjectName(u"tw_setor_18")

        self.verticalLayout_30.addWidget(self.tw_setor_18)


        self.gridLayout_6.addWidget(self.frame_setor_18, 6, 2, 1, 1)

        self.frame_setor_19 = QFrame(self.frameExib)
        self.frame_setor_19.setObjectName(u"frame_setor_19")
        self.frame_setor_19.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.frame_setor_19.sizePolicy().hasHeightForWidth())
        self.frame_setor_19.setSizePolicy(sizePolicy1)
        self.frame_setor_19.setFrameShape(QFrame.StyledPanel)
        self.frame_setor_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_setor_19)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_setor_19 = QLabel(self.frame_setor_19)
        self.label_setor_19.setObjectName(u"label_setor_19")
        sizePolicy2.setHeightForWidth(self.label_setor_19.sizePolicy().hasHeightForWidth())
        self.label_setor_19.setSizePolicy(sizePolicy2)
        self.label_setor_19.setMaximumSize(QSize(16777215, 20))
        self.label_setor_19.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_setor_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.label_setor_19)

        self.tw_setor_19 = QTreeWidget(self.frame_setor_19)
        self.tw_setor_19.setObjectName(u"tw_setor_19")

        self.verticalLayout_31.addWidget(self.tw_setor_19)


        self.gridLayout_6.addWidget(self.frame_setor_19, 7, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frameExib, 1, 0, 1, 1)

        self.txtBarCodeExib = QLineEdit(self.tabExib)
        self.txtBarCodeExib.setObjectName(u"txtBarCodeExib")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txtBarCodeExib.sizePolicy().hasHeightForWidth())
        self.txtBarCodeExib.setSizePolicy(sizePolicy3)
        self.txtBarCodeExib.setMaximumSize(QSize(200, 16777215))
        self.txtBarCodeExib.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txtBarCodeExib, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabExib, "")
        self.tabCadInt = QWidget()
        self.tabCadInt.setObjectName(u"tabCadInt")
        self.tabCadInt.setMaximumSize(QSize(700, 700))
        self.gridLayout = QGridLayout(self.tabCadInt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_6 = QFrame(self.tabCadInt)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnAtualizar = QPushButton(self.frame_6)
        self.btnAtualizar.setObjectName(u"btnAtualizar")
        self.btnAtualizar.setMaximumSize(QSize(120, 16777215))
        self.btnAtualizar.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.btnAtualizar)


        self.gridLayout.addWidget(self.frame_6, 4, 1, 1, 1)

        self.frame_5 = QFrame(self.tabCadInt)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(400, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.treeInternos = QTreeWidget(self.frame_5)
        self.treeInternos.setObjectName(u"treeInternos")
        sizePolicy.setHeightForWidth(self.treeInternos.sizePolicy().hasHeightForWidth())
        self.treeInternos.setSizePolicy(sizePolicy)
        self.treeInternos.setMaximumSize(QSize(390, 16777215))
        self.treeInternos.setFrameShape(QFrame.StyledPanel)
        self.treeInternos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.horizontalLayout_4.addWidget(self.treeInternos)


        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_2 = QFrame(self.tabCadInt)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(250, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txtNome = QLineEdit(self.frame_2)
        self.txtNome.setObjectName(u"txtNome")
        self.txtNome.setMaximumSize(QSize(167, 16777215))

        self.verticalLayout_3.addWidget(self.txtNome)

        self.txtRGI = QLineEdit(self.frame_2)
        self.txtRGI.setObjectName(u"txtRGI")
        self.txtRGI.setMaximumSize(QSize(167, 16777215))

        self.verticalLayout_3.addWidget(self.txtRGI)

        self.txtCela = QLineEdit(self.frame_2)
        self.txtCela.setObjectName(u"txtCela")
        self.txtCela.setMaximumSize(QSize(167, 16777215))

        self.verticalLayout_3.addWidget(self.txtCela)

        self.cbbSetor = QComboBox(self.frame_2)
        self.cbbSetor.setObjectName(u"cbbSetor")
        self.cbbSetor.setMaximumSize(QSize(167, 16777215))

        self.verticalLayout_3.addWidget(self.cbbSetor)

        self.txtBarCode = QLineEdit(self.frame_2)
        self.txtBarCode.setObjectName(u"txtBarCode")
        self.txtBarCode.setMaximumSize(QSize(167, 16777215))

        self.verticalLayout_3.addWidget(self.txtBarCode)

        self.tbFoto = QToolButton(self.frame_2)
        self.tbFoto.setObjectName(u"tbFoto")

        self.verticalLayout_3.addWidget(self.tbFoto)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.tabCadInt)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.gridLayout.addWidget(self.frame_4, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.tabCadInt)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(250, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSalvar = QPushButton(self.frame_3)
        self.btnSalvar.setObjectName(u"btnSalvar")
        self.btnSalvar.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_2.addWidget(self.btnSalvar)

        self.btnDeletar = QPushButton(self.frame_3)
        self.btnDeletar.setObjectName(u"btnDeletar")
        self.btnDeletar.setMaximumSize(QSize(120, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.btnDeletar.setPalette(palette)

        self.horizontalLayout_2.addWidget(self.btnDeletar)


        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1)

        self.frame = QFrame(self.tabCadInt)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabCadInt, "")
        self.tabGerSet = QWidget()
        self.tabGerSet.setObjectName(u"tabGerSet")
        self.gridLayout_2 = QGridLayout(self.tabGerSet)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_10 = QFrame(self.tabGerSet)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 120))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnSalvarSetor = QPushButton(self.frame_10)
        self.btnSalvarSetor.setObjectName(u"btnSalvarSetor")
        self.btnSalvarSetor.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_5.addWidget(self.btnSalvarSetor)

        self.btnDeletarCadastro = QPushButton(self.frame_10)
        self.btnDeletarCadastro.setObjectName(u"btnDeletarCadastro")
        self.btnDeletarCadastro.setMaximumSize(QSize(120, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.btnDeletarCadastro.setPalette(palette1)

        self.horizontalLayout_5.addWidget(self.btnDeletarCadastro)


        self.gridLayout_2.addWidget(self.frame_10, 3, 0, 1, 1)

        self.frame_8 = QFrame(self.tabGerSet)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 120))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_4)


        self.gridLayout_2.addWidget(self.frame_8, 0, 1, 1, 1)

        self.frame_12 = QFrame(self.tabGerSet)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 300))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btnAtualizarSetor = QPushButton(self.frame_12)
        self.btnAtualizarSetor.setObjectName(u"btnAtualizarSetor")
        self.btnAtualizarSetor.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout.addWidget(self.btnAtualizarSetor)


        self.gridLayout_2.addWidget(self.frame_12, 3, 1, 1, 1)

        self.frame_11 = QFrame(self.tabGerSet)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setMaximumSize(QSize(16777215, 450))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.treeSetores = QTreeWidget(self.frame_11)
        font = QFont()
        font.setPointSize(10)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font);
        __qtreewidgetitem.setBackground(0, QColor(255, 255, 0));
        self.treeSetores.setHeaderItem(__qtreewidgetitem)
        self.treeSetores.setObjectName(u"treeSetores")
        self.treeSetores.setEnabled(True)
        self.treeSetores.setMaximumSize(QSize(300, 500))

        self.horizontalLayout_6.addWidget(self.treeSetores)


        self.gridLayout_2.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.tabGerSet)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 120))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 120))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)


        self.gridLayout_2.addWidget(self.frame_7, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.tabGerSet)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy4.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy4)
        self.frame_9.setMaximumSize(QSize(250, 450))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.txtSetorCadastro = QLineEdit(self.frame_9)
        self.txtSetorCadastro.setObjectName(u"txtSetorCadastro")
        self.txtSetorCadastro.setMaximumSize(QSize(167, 16777215))
        self.txtSetorCadastro.setLayoutDirection(Qt.LeftToRight)
        self.txtSetorCadastro.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.txtSetorCadastro)

        self.lblCor = QLabel(self.frame_9)
        self.lblCor.setObjectName(u"lblCor")
        self.lblCor.setMaximumSize(QSize(167, 30))
        self.lblCor.setStyleSheet(u"background-color: rgb(0, 255, 255);")

        self.verticalLayout_6.addWidget(self.lblCor)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addWidget(self.frame_9, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabGerSet, "")
        self.tabContVideo = QWidget()
        self.tabContVideo.setObjectName(u"tabContVideo")
        self.gridLayout_3 = QGridLayout(self.tabContVideo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_13 = QFrame(self.tabContVideo)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.gridLayout_3.addWidget(self.frame_13, 0, 0, 1, 1)

        self.frame_14 = QFrame(self.tabContVideo)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_14, 0, 2, 1, 1)

        self.frame_15 = QFrame(self.tabContVideo)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setEnabled(True)
        self.frame_15.setMaximumSize(QSize(16777215, 500))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txtNomeAud = QLineEdit(self.frame_15)
        self.txtNomeAud.setObjectName(u"txtNomeAud")

        self.verticalLayout_10.addWidget(self.txtNomeAud)

        self.txtCelaAud = QLineEdit(self.frame_15)
        self.txtCelaAud.setObjectName(u"txtCelaAud")

        self.verticalLayout_10.addWidget(self.txtCelaAud)

        self.verticalSpacer_3 = QSpacerItem(20, 350, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addWidget(self.frame_15, 1, 0, 1, 1)

        self.frame_17 = QFrame(self.tabContVideo)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(16777215, 500))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.twAudiencia = QTreeWidget(self.frame_17)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"Nome");
        self.twAudiencia.setHeaderItem(__qtreewidgetitem1)
        self.twAudiencia.setObjectName(u"twAudiencia")

        self.verticalLayout_11.addWidget(self.twAudiencia)


        self.gridLayout_3.addWidget(self.frame_17, 1, 2, 1, 1)

        self.frame_16 = QFrame(self.tabContVideo)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.pbEntradaAud = QPushButton(self.frame_16)
        self.pbEntradaAud.setObjectName(u"pbEntradaAud")
        self.pbEntradaAud.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.pbEntradaAud)

        self.btnSaidaAud = QPushButton(self.frame_16)
        self.btnSaidaAud.setObjectName(u"btnSaidaAud")
        self.btnSaidaAud.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.btnSaidaAud)


        self.gridLayout_3.addWidget(self.frame_16, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tabContVideo, "")
        self.tabAtendimento = QWidget()
        self.tabAtendimento.setObjectName(u"tabAtendimento")
        self.gridLayout_5 = QGridLayout(self.tabAtendimento)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_18 = QFrame(self.tabAtendimento)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_18)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lblAtendimento = QLabel(self.frame_18)
        self.lblAtendimento.setObjectName(u"lblAtendimento")
        self.lblAtendimento.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.lblAtendimento)


        self.gridLayout_5.addWidget(self.frame_18, 0, 0, 1, 1)

        self.frame_19 = QFrame(self.tabAtendimento)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_19, 0, 1, 1, 1)

        self.widget = QWidget(self.tabAtendimento)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(167, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.widget)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.txtNomeAtend = QLineEdit(self.widget)
        self.txtNomeAtend.setObjectName(u"txtNomeAtend")

        self.verticalLayout_12.addWidget(self.txtNomeAtend)

        self.txtCelaAtend = QLineEdit(self.widget)
        self.txtCelaAtend.setObjectName(u"txtCelaAtend")

        self.verticalLayout_12.addWidget(self.txtCelaAtend)

        self.cbbAtend = QComboBox(self.widget)
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.addItem("")
        self.cbbAtend.setObjectName(u"cbbAtend")

        self.verticalLayout_12.addWidget(self.cbbAtend)

        self.verticalSpacer_4 = QSpacerItem(20, 350, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_12.addItem(self.verticalSpacer_4)


        self.gridLayout_5.addWidget(self.widget, 1, 0, 1, 1)

        self.frame_21 = QFrame(self.tabAtendimento)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btnEntAtend = QPushButton(self.frame_21)
        self.btnEntAtend.setObjectName(u"btnEntAtend")
        self.btnEntAtend.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_9.addWidget(self.btnEntAtend)

        self.btnSaiAtend = QPushButton(self.frame_21)
        self.btnSaiAtend.setObjectName(u"btnSaiAtend")
        self.btnSaiAtend.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_9.addWidget(self.btnSaiAtend)


        self.gridLayout_5.addWidget(self.frame_21, 2, 0, 1, 1)

        self.frame_22 = QFrame(self.tabAtendimento)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.gridLayout_5.addWidget(self.frame_22, 2, 1, 1, 1)

        self.frame_20 = QFrame(self.tabAtendimento)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 500))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.treeAtendimento = QTreeWidget(self.frame_20)
        self.treeAtendimento.setObjectName(u"treeAtendimento")
        self.treeAtendimento.setMaximumSize(QSize(300, 500))

        self.verticalLayout_7.addWidget(self.treeAtendimento)


        self.gridLayout_5.addWidget(self.frame_20, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tabAtendimento, "")
        self.tabRelatorio = QWidget()
        self.tabRelatorio.setObjectName(u"tabRelatorio")
        self.gridLayout_8 = QGridLayout(self.tabRelatorio)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_24 = QFrame(self.tabRelatorio)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_24)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.checkBox = QCheckBox(self.frame_24)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_9.addWidget(self.checkBox, 1, 0, 1, 1)

        self.dateTimeEdit = QDateTimeEdit(self.frame_24)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setDate(QDate(2000, 1, 13))

        self.gridLayout_9.addWidget(self.dateTimeEdit, 5, 0, 1, 2)

        self.checkBox_3 = QCheckBox(self.frame_24)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_9.addWidget(self.checkBox_3, 3, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame_24)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_9.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.dateTimeEdit_2 = QDateTimeEdit(self.frame_24)
        self.dateTimeEdit_2.setObjectName(u"dateTimeEdit_2")

        self.gridLayout_9.addWidget(self.dateTimeEdit_2, 6, 0, 1, 2)

        self.pushButton = QPushButton(self.frame_24)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_9.addWidget(self.pushButton, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_24)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_9.addWidget(self.pushButton_2, 4, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame_24, 1, 0, 1, 1)

        self.frame_23 = QFrame(self.tabRelatorio)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_23)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 90, 47, 13))

        self.gridLayout_8.addWidget(self.frame_23, 0, 0, 1, 1)

        self.frame_25 = QFrame(self.tabRelatorio)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_25, 0, 1, 1, 1)

        self.frame_26 = QFrame(self.tabRelatorio)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.tableView = QTableView(self.frame_26)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(70, 40, 256, 192))

        self.gridLayout_8.addWidget(self.frame_26, 1, 1, 1, 1)

        self.frame_27 = QFrame(self.tabRelatorio)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.frame_27)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(80, 200, 75, 23))
        self.pushButton_4 = QPushButton(self.frame_27)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(260, 200, 75, 23))

        self.gridLayout_8.addWidget(self.frame_27, 2, 0, 1, 1)

        self.frame_28 = QFrame(self.tabRelatorio)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)

        self.gridLayout_8.addWidget(self.frame_28, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tabRelatorio, "")

        self.verticalLayout_9.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_setor_7.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem = self.tw_setor_7.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_3.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem1 = self.tw_setor_3.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_10.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem2 = self.tw_setor_10.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_11.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem3 = self.tw_setor_11.headerItem()
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_4.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem4 = self.tw_setor_4.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_1.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem5 = self.tw_setor_1.headerItem()
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_20.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem6 = self.tw_setor_20.headerItem()
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_14.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem7 = self.tw_setor_14.headerItem()
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_6.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem8 = self.tw_setor_6.headerItem()
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_13.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem9 = self.tw_setor_13.headerItem()
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_9.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem10 = self.tw_setor_9.headerItem()
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_8.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem11 = self.tw_setor_8.headerItem()
        ___qtreewidgetitem11.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_5.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem12 = self.tw_setor_5.headerItem()
        ___qtreewidgetitem12.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_12.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem13 = self.tw_setor_12.headerItem()
        ___qtreewidgetitem13.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_2.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem14 = self.tw_setor_2.headerItem()
        ___qtreewidgetitem14.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_15.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem15 = self.tw_setor_15.headerItem()
        ___qtreewidgetitem15.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_16.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem16 = self.tw_setor_16.headerItem()
        ___qtreewidgetitem16.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_17.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem17 = self.tw_setor_17.headerItem()
        ___qtreewidgetitem17.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_18.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem18 = self.tw_setor_18.headerItem()
        ___qtreewidgetitem18.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem18.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.label_setor_19.setText(QCoreApplication.translate("Widget", u"SETOR", None))
        ___qtreewidgetitem19 = self.tw_setor_19.headerItem()
        ___qtreewidgetitem19.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem19.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.txtBarCodeExib.setText(QCoreApplication.translate("Widget", u"C\u00f3digo de barras", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExib), QCoreApplication.translate("Widget", u"Exibi\u00e7\u00e3o", None))
        self.btnAtualizar.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        ___qtreewidgetitem20 = self.treeInternos.headerItem()
        ___qtreewidgetitem20.setText(2, QCoreApplication.translate("Widget", u"Setor", None));
        ___qtreewidgetitem20.setText(1, QCoreApplication.translate("Widget", u"RGI", None));
        ___qtreewidgetitem20.setText(0, QCoreApplication.translate("Widget", u"Nome", None));
        self.txtNome.setText(QCoreApplication.translate("Widget", u"Nome", None))
        self.txtRGI.setText(QCoreApplication.translate("Widget", u"RGI", None))
        self.txtCela.setText(QCoreApplication.translate("Widget", u"Cela", None))
#if QT_CONFIG(tooltip)
        self.cbbSetor.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>Setor</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbbSetor.setCurrentText("")
        self.txtBarCode.setText(QCoreApplication.translate("Widget", u"Codigo de Barras", None))
        self.tbFoto.setText(QCoreApplication.translate("Widget", u"Selecionar Foto", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Internos cadastrados</span></p></body></html>", None))
        self.btnSalvar.setText(QCoreApplication.translate("Widget", u"Salvar", None))
        self.btnDeletar.setText(QCoreApplication.translate("Widget", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Cadastrar/Editar Internos</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCadInt), QCoreApplication.translate("Widget", u"Cadastro de internos", None))
        self.btnSalvarSetor.setText(QCoreApplication.translate("Widget", u"Salvar", None))
        self.btnDeletarCadastro.setText(QCoreApplication.translate("Widget", u"Deletar", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Setores Cadastrados</span></p></body></html>", None))
        self.btnAtualizarSetor.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        ___qtreewidgetitem21 = self.treeSetores.headerItem()
        ___qtreewidgetitem21.setText(0, QCoreApplication.translate("Widget", u"Setores", None));
        self.label_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Cadastrar/Atualizar Setores</span></p></body></html>", None))
        self.txtSetorCadastro.setText(QCoreApplication.translate("Widget", u"Setor", None))
        self.lblCor.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGerSet), QCoreApplication.translate("Widget", u"Gerenciamento Setores", None))
#if QT_CONFIG(accessibility)
        self.tabContVideo.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Internos em Audi\u00eancia</span></p></body></html>", None))
        self.txtNomeAud.setText(QCoreApplication.translate("Widget", u"Nome", None))
        self.txtCelaAud.setText(QCoreApplication.translate("Widget", u"Cela", None))
        ___qtreewidgetitem22 = self.twAudiencia.headerItem()
        ___qtreewidgetitem22.setText(1, QCoreApplication.translate("Widget", u"Cela", None));
        self.pbEntradaAud.setText(QCoreApplication.translate("Widget", u"Entrada", None))
        self.btnSaidaAud.setText(QCoreApplication.translate("Widget", u"Saida", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabContVideo), QCoreApplication.translate("Widget", u"Controle Video", None))
        self.lblAtendimento.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Atendimento</span></p></body></html>", None))
        self.txtNomeAtend.setText(QCoreApplication.translate("Widget", u"Nome", None))
        self.txtCelaAtend.setText(QCoreApplication.translate("Widget", u"Cela", None))
        self.cbbAtend.setItemText(0, QCoreApplication.translate("Widget", u"MEDICO", None))
        self.cbbAtend.setItemText(1, QCoreApplication.translate("Widget", u"DENTISTA", None))
        self.cbbAtend.setItemText(2, QCoreApplication.translate("Widget", u"ASSITENCIA SOCIAL", None))
        self.cbbAtend.setItemText(3, QCoreApplication.translate("Widget", u"PSICOLOGA", None))
        self.cbbAtend.setItemText(4, QCoreApplication.translate("Widget", u"SEGURAN\u00c7A", None))
        self.cbbAtend.setItemText(5, QCoreApplication.translate("Widget", u"DISCIPLINA", None))
        self.cbbAtend.setItemText(6, QCoreApplication.translate("Widget", u"JURIDICO", None))
        self.cbbAtend.setItemText(7, QCoreApplication.translate("Widget", u"TRABALHO", None))
        self.cbbAtend.setItemText(8, QCoreApplication.translate("Widget", u"OUTROS", None))

        self.btnEntAtend.setText(QCoreApplication.translate("Widget", u"Entrada", None))
        self.btnSaiAtend.setText(QCoreApplication.translate("Widget", u"Saida", None))
        ___qtreewidgetitem23 = self.treeAtendimento.headerItem()
        ___qtreewidgetitem23.setText(2, QCoreApplication.translate("Widget", u"SETOR", None));
        ___qtreewidgetitem23.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem23.setText(0, QCoreApplication.translate("Widget", u"NOME", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAtendimento), QCoreApplication.translate("Widget", u"Atendimento", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.checkBox_3.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("Widget", u"CheckBox", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRelatorio), QCoreApplication.translate("Widget", u"Page", None))
    # retranslateUi

