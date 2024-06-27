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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(817, 739)
        self.verticalLayout_7 = QVBoxLayout(Widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tabWidget = QTabWidget(Widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabExib = QWidget()
        self.tabExib.setObjectName(u"tabExib")
        self.gridLayout_4 = QGridLayout(self.tabExib)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.twLixo = QTreeWidget(self.tabExib)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"LIXO/ESGOTO/RECICLAGEM");
        self.twLixo.setHeaderItem(__qtreewidgetitem)
        self.twLixo.setObjectName(u"twLixo")

        self.gridLayout_4.addWidget(self.twLixo, 3, 1, 1, 2)

        self.twJardin = QTreeWidget(self.tabExib)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"JARDINAGEM");
        self.twJardin.setHeaderItem(__qtreewidgetitem1)
        self.twJardin.setObjectName(u"twJardin")

        self.gridLayout_4.addWidget(self.twJardin, 2, 3, 1, 2)

        self.twEletricista = QTreeWidget(self.tabExib)
        __qtreewidgetitem2 = QTreeWidgetItem()
        __qtreewidgetitem2.setText(0, u"ELETRICISTA");
        self.twEletricista.setHeaderItem(__qtreewidgetitem2)
        self.twEletricista.setObjectName(u"twEletricista")

        self.gridLayout_4.addWidget(self.twEletricista, 3, 3, 1, 2)

        self.twHorta = QTreeWidget(self.tabExib)
        __qtreewidgetitem3 = QTreeWidgetItem()
        __qtreewidgetitem3.setText(0, u"HORTA");
        self.twHorta.setHeaderItem(__qtreewidgetitem3)
        self.twHorta.setObjectName(u"twHorta")

        self.gridLayout_4.addWidget(self.twHorta, 1, 3, 1, 2)

        self.twCostura = QTreeWidget(self.tabExib)
        __qtreewidgetitem4 = QTreeWidgetItem()
        __qtreewidgetitem4.setText(0, u"COSTURA");
        self.twCostura.setHeaderItem(__qtreewidgetitem4)
        self.twCostura.setObjectName(u"twCostura")

        self.gridLayout_4.addWidget(self.twCostura, 2, 1, 1, 2)

        self.twObra = QTreeWidget(self.tabExib)
        __qtreewidgetitem5 = QTreeWidgetItem()
        __qtreewidgetitem5.setText(0, u"OBRA");
        self.twObra.setHeaderItem(__qtreewidgetitem5)
        self.twObra.setObjectName(u"twObra")

        self.gridLayout_4.addWidget(self.twObra, 2, 0, 1, 1)

        self.twFaxina = QTreeWidget(self.tabExib)
        __qtreewidgetitem6 = QTreeWidgetItem()
        __qtreewidgetitem6.setText(0, u"FAXINA");
        self.twFaxina.setHeaderItem(__qtreewidgetitem6)
        self.twFaxina.setObjectName(u"twFaxina")

        self.gridLayout_4.addWidget(self.twFaxina, 1, 1, 1, 2)

        self.twPrendedor = QTreeWidget(self.tabExib)
        __qtreewidgetitem7 = QTreeWidgetItem()
        __qtreewidgetitem7.setText(0, u"PRENDEDOR");
        self.twPrendedor.setHeaderItem(__qtreewidgetitem7)
        self.twPrendedor.setObjectName(u"twPrendedor")

        self.gridLayout_4.addWidget(self.twPrendedor, 1, 0, 1, 1)

        self.twCopa = QTreeWidget(self.tabExib)
        __qtreewidgetitem8 = QTreeWidgetItem()
        __qtreewidgetitem8.setText(0, u"COPA");
        self.twCopa.setHeaderItem(__qtreewidgetitem8)
        self.twCopa.setObjectName(u"twCopa")

        self.gridLayout_4.addWidget(self.twCopa, 0, 3, 1, 2)

        self.twAdm = QTreeWidget(self.tabExib)
        __qtreewidgetitem9 = QTreeWidgetItem()
        __qtreewidgetitem9.setText(0, u"ADMINISTRATIVO");
        self.twAdm.setHeaderItem(__qtreewidgetitem9)
        self.twAdm.setObjectName(u"twAdm")

        self.gridLayout_4.addWidget(self.twAdm, 0, 1, 1, 2)

        self.twCozinha = QTreeWidget(self.tabExib)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtreewidgetitem10 = QTreeWidgetItem()
        __qtreewidgetitem10.setText(0, u"COZINHA");
        __qtreewidgetitem10.setBackground(0, QColor(255, 62, 48));
        __qtreewidgetitem10.setForeground(0, brush);
        self.twCozinha.setHeaderItem(__qtreewidgetitem10)
        font = QFont()
        font.setUnderline(True)
        __qtreewidgetitem11 = QTreeWidgetItem(self.twCozinha)
        __qtreewidgetitem11.setFont(0, font);
        self.twCozinha.setObjectName(u"twCozinha")

        self.gridLayout_4.addWidget(self.twCozinha, 0, 0, 1, 1)

        self.twSerra = QTreeWidget(self.tabExib)
        __qtreewidgetitem12 = QTreeWidgetItem()
        __qtreewidgetitem12.setText(0, u"SERRALHERIA");
        self.twSerra.setHeaderItem(__qtreewidgetitem12)
        self.twSerra.setObjectName(u"twSerra")

        self.gridLayout_4.addWidget(self.twSerra, 3, 0, 1, 1)

        self.txtBarCodeExib = QLineEdit(self.tabExib)
        self.txtBarCodeExib.setObjectName(u"txtBarCodeExib")
        self.txtBarCodeExib.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.txtBarCodeExib, 4, 1, 1, 1)

        self.tabWidget.addTab(self.tabExib, "")
        self.tabCadInt = QWidget()
        self.tabCadInt.setObjectName(u"tabCadInt")
        self.gridLayout = QGridLayout(self.tabCadInt)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.tabCadInt)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(400, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.treeInternos = QTreeWidget(self.frame_5)
        self.treeInternos.setObjectName(u"treeInternos")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeInternos.sizePolicy().hasHeightForWidth())
        self.treeInternos.setSizePolicy(sizePolicy)
        self.treeInternos.setMaximumSize(QSize(390, 16777215))
        self.treeInternos.setFrameShape(QFrame.StyledPanel)
        self.treeInternos.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.horizontalLayout_4.addWidget(self.treeInternos)


        self.gridLayout.addWidget(self.frame_5, 1, 1, 1, 1)

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


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tabCadInt, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_10 = QFrame(self.tab_3)
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

        self.frame_8 = QFrame(self.tab_3)
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

        self.frame_12 = QFrame(self.tab_3)
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

        self.frame_11 = QFrame(self.tab_3)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy1)
        self.frame_11.setMaximumSize(QSize(16777215, 500))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.treeSetores = QTreeWidget(self.frame_11)
        font1 = QFont()
        font1.setPointSize(10)
        __qtreewidgetitem13 = QTreeWidgetItem()
        __qtreewidgetitem13.setFont(0, font1);
        __qtreewidgetitem13.setBackground(0, QColor(255, 255, 0));
        self.treeSetores.setHeaderItem(__qtreewidgetitem13)
        brush3 = QBrush(QColor(255, 85, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        brush4 = QBrush(QColor(0, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        __qtreewidgetitem14 = QTreeWidgetItem(self.treeSetores)
        __qtreewidgetitem14.setBackground(0, brush3);
        __qtreewidgetitem15 = QTreeWidgetItem(self.treeSetores)
        __qtreewidgetitem15.setBackground(0, brush4);
        self.treeSetores.setObjectName(u"treeSetores")
        self.treeSetores.setMaximumSize(QSize(300, 500))

        self.horizontalLayout_6.addWidget(self.treeSetores)


        self.gridLayout_2.addWidget(self.frame_11, 1, 1, 1, 1)

        self.frame_7 = QFrame(self.tab_3)
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

        self.frame_9 = QFrame(self.tab_3)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setMaximumSize(QSize(250, 16777215))
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

        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_13 = QFrame(self.tab)
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

        self.frame_14 = QFrame(self.tab)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.frame_14, 0, 2, 1, 1)

        self.frame_15 = QFrame(self.tab)
        self.frame_15.setObjectName(u"frame_15")
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

        self.verticalSpacer_3 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_10.addItem(self.verticalSpacer_3)


        self.gridLayout_3.addWidget(self.frame_15, 1, 0, 1, 1)

        self.frame_17 = QFrame(self.tab)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.twAudiencia = QTreeWidget(self.frame_17)
        __qtreewidgetitem16 = QTreeWidgetItem()
        __qtreewidgetitem16.setText(0, u"Internos");
        self.twAudiencia.setHeaderItem(__qtreewidgetitem16)
        self.twAudiencia.setObjectName(u"twAudiencia")

        self.verticalLayout_11.addWidget(self.twAudiencia)


        self.gridLayout_3.addWidget(self.frame_17, 1, 2, 1, 1)

        self.frame_16 = QFrame(self.tab)
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

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_7.addWidget(self.tabWidget)


        self.retranslateUi(Widget)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        ___qtreewidgetitem = self.twLixo.headerItem()
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem1 = self.twJardin.headerItem()
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem2 = self.twEletricista.headerItem()
        ___qtreewidgetitem2.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem3 = self.twHorta.headerItem()
        ___qtreewidgetitem3.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem4 = self.twCostura.headerItem()
        ___qtreewidgetitem4.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem5 = self.twObra.headerItem()
        ___qtreewidgetitem5.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem6 = self.twFaxina.headerItem()
        ___qtreewidgetitem6.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem7 = self.twPrendedor.headerItem()
        ___qtreewidgetitem7.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem8 = self.twCopa.headerItem()
        ___qtreewidgetitem8.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem9 = self.twAdm.headerItem()
        ___qtreewidgetitem9.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        ___qtreewidgetitem10 = self.twCozinha.headerItem()
        ___qtreewidgetitem10.setText(1, QCoreApplication.translate("Widget", u"CELA", None));

        __sortingEnabled = self.twCozinha.isSortingEnabled()
        self.twCozinha.setSortingEnabled(False)
        self.twCozinha.setSortingEnabled(__sortingEnabled)

        ___qtreewidgetitem11 = self.twSerra.headerItem()
        ___qtreewidgetitem11.setText(1, QCoreApplication.translate("Widget", u"CELA", None));
        self.txtBarCodeExib.setText(QCoreApplication.translate("Widget", u"C\u00f3digo de barras", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExib), QCoreApplication.translate("Widget", u"Exibi\u00e7\u00e3o", None))
        ___qtreewidgetitem12 = self.treeInternos.headerItem()
        ___qtreewidgetitem12.setText(2, QCoreApplication.translate("Widget", u"Setor", None));
        ___qtreewidgetitem12.setText(1, QCoreApplication.translate("Widget", u"RGI", None));
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("Widget", u"Nome", None));
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Internos cadastrados</span></p></body></html>", None))
        self.btnAtualizar.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        self.btnSalvar.setText(QCoreApplication.translate("Widget", u"Salvar", None))
        self.btnDeletar.setText(QCoreApplication.translate("Widget", u"Deletar", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Cadastrar/Editar Internos</span></p></body></html>", None))
        self.txtNome.setText(QCoreApplication.translate("Widget", u"Nome", None))
        self.txtRGI.setText(QCoreApplication.translate("Widget", u"RGI", None))
        self.txtCela.setText(QCoreApplication.translate("Widget", u"Cela", None))
#if QT_CONFIG(tooltip)
        self.cbbSetor.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>Setor</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cbbSetor.setCurrentText("")
        self.txtBarCode.setText(QCoreApplication.translate("Widget", u"Codigo de Barras", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCadInt), QCoreApplication.translate("Widget", u"Cadastro de internos", None))
        self.btnSalvarSetor.setText(QCoreApplication.translate("Widget", u"Salvar", None))
        self.btnDeletarCadastro.setText(QCoreApplication.translate("Widget", u"Deletar", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Setores Cadastrados</span></p></body></html>", None))
        self.btnAtualizarSetor.setText(QCoreApplication.translate("Widget", u"Atualizar", None))
        ___qtreewidgetitem13 = self.treeSetores.headerItem()
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("Widget", u"Setores", None));

        __sortingEnabled1 = self.treeSetores.isSortingEnabled()
        self.treeSetores.setSortingEnabled(False)
        ___qtreewidgetitem14 = self.treeSetores.topLevelItem(0)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("Widget", u"Cozinha", None));
        ___qtreewidgetitem15 = self.treeSetores.topLevelItem(1)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("Widget", u"Administrativo", None));
        self.treeSetores.setSortingEnabled(__sortingEnabled1)

        self.label_3.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; vertical-align:super;\">Cadastrar/Atualizar Setores</span></p></body></html>", None))
        self.txtSetorCadastro.setText(QCoreApplication.translate("Widget", u"Setor", None))
        self.lblCor.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Widget", u"Gerenciamento Setores", None))
#if QT_CONFIG(accessibility)
        self.tab.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.label_6.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; vertical-align:super;\">Internos em Audi\u00eancia</span></p></body></html>", None))
        self.txtNomeAud.setText(QCoreApplication.translate("Widget", u"Nome", None))
        self.txtCelaAud.setText(QCoreApplication.translate("Widget", u"Cela", None))
        self.pbEntradaAud.setText(QCoreApplication.translate("Widget", u"Entrada", None))
        self.btnSaidaAud.setText(QCoreApplication.translate("Widget", u"Saida", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Widget", u"Controle Video", None))
    # retranslateUi

