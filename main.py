# main.py

import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QColorDialog, QMessageBox, QTreeWidgetItem, QFileDialog, QDialog, QVBoxLayout, QLabel, QPushButton
from form import Ui_Widget
from PySide6.QtGui import QColor, QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect('controle.db')
        self.cursor = self.connection.cursor()
        self.create_tables()
        self.ui.lblCor.mousePressEvent = self.choose_color
        self.ui.btnSalvarSetor.clicked.connect(self.save_setor)
        self.ui.btnAtualizarSetor.clicked.connect(self.load_setores)
        self.ui.btnDeletarCadastro.clicked.connect(self.delete_setor)
        self.ui.btnSalvar.clicked.connect(self.save_interno)
        self.ui.tbFoto.clicked.connect(self.select_photo)
        self.ui.treeInternos.itemDoubleClicked.connect(self.show_interno_details)
        self.ui.btnDeletar.clicked.connect(self.delete_interno)
        self.load_setores()
        self.load_internos()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS setores (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                cor TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS internos (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                rgi TEXT NOT NULL,
                                cela TEXT NOT NULL,
                                barcode TEXT NOT NULL,
                                setor TEXT NOT NULL,
                                foto TEXT)''')
        self.connection.commit()

    def choose_color(self, event):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.lblCor.setStyleSheet(f'background-color: {color.name()}')
            self.ui.lblCor.setText(color.name())

    def save_setor(self):
        nome = self.ui.txtSetorCadastro.text().upper()
        cor = self.ui.lblCor.text().upper()
        if nome and cor:
            self.cursor.execute('INSERT INTO setores (nome, cor) VALUES (?, ?)', (nome, cor))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Setor cadastrado com sucesso!')
            self.load_setores()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, preencha todos os campos.')

    def load_setores(self):
        self.ui.treeSetores.clear()
        self.ui.cbbSetor.clear()
        self.cursor.execute('SELECT nome, cor FROM setores')
        setores = self.cursor.fetchall()
        for setor in setores:
            item = QTreeWidgetItem([setor[0], setor[1]])
            item.setBackground(0, QColor(setor[1]))
            item.setBackground(1, QColor(setor[1]))
            self.ui.treeSetores.addTopLevelItem(item)
            self.ui.cbbSetor.addItem(setor[0])

    def delete_setor(self):
        selected_item = self.ui.treeSetores.currentItem()
        if selected_item:
            nome = selected_item.text(0)
            self.cursor.execute('DELETE FROM setores WHERE nome = ?', (nome,))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Setor deletado com sucesso!')
            self.load_setores()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, selecione um setor para deletar.')

    def select_photo(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Photo", "", "Images (*.png *.xpm *.jpg)", options=options)
        if file_name:
            self.ui.tbFoto.setText(file_name)

    def save_interno(self):
        nome = self.ui.txtNome.text().upper()
        rgi = self.ui.txtRGI.text().upper()
        cela = self.ui.txtCela.text().upper()
        barcode = self.ui.txtBarCode.text().upper()
        setor = self.ui.cbbSetor.currentText().upper()
        foto = self.ui.tbFoto.text()
        if nome and rgi and cela and barcode and setor:
            self.cursor.execute('INSERT INTO internos (nome, rgi, cela, barcode, setor, foto) VALUES (?, ?, ?, ?, ?, ?)', (nome, rgi, cela, barcode, setor, foto))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Interno cadastrado com sucesso!')
            self.load_internos()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, preencha todos os campos.')

    def load_internos(self):
        self.ui.treeInternos.clear()
        self.cursor.execute('SELECT nome, rgi, setor, cela FROM internos')
        internos = self.cursor.fetchall()
        for interno in internos:
            item = QTreeWidgetItem([interno[0], interno[1], interno[2], interno[3]])
            self.ui.treeInternos.addTopLevelItem(item)

    def show_interno_details(self, item):
        nome = item.text(0)
        self.cursor.execute('SELECT * FROM internos WHERE nome = ?', (nome,))
        interno = self.cursor.fetchone()
        if interno:
            dialog = QDialog(self)
            dialog.setWindowTitle("Detalhes do Interno")
            dialog.setGeometry(100, 100, 400, 300)
            layout = QVBoxLayout()
            label_foto = QLabel()
            if interno[6]:
                pixmap = QPixmap(interno[6])
                label_foto.setPixmap(pixmap.scaled(100, 100))
            label_nome = QLabel(f"Nome: {interno[1]}")
            label_rgi = QLabel(f"RGI: {interno[2]}")
            label_cela = QLabel(f"Cela: {interno[3]}")
            label_barcode = QLabel(f"Código de Barras: {interno[4]}")
            label_setor = QLabel(f"Setor: {interno[5]}")
            layout.addWidget(label_foto)
            layout.addWidget(label_nome)
            layout.addWidget(label_rgi)
            layout.addWidget(label_cela)            
            layout.addWidget(label_setor)
            layout.addWidget(label_barcode)
            dialog.setLayout(layout)
            dialog.exec()

    def delete_interno(self):
        selected_item = self.ui.treeInternos.currentItem()
        if selected_item:
            nome = selected_item.text(0)
            reply = QMessageBox.question(self, 'Confirmar Exclusão', f'Tem certeza que deseja excluir o interno {nome}?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cursor.execute('DELETE FROM internos WHERE nome = ?', (nome,))
                self.connection.commit()
                QMessageBox.information(self, 'Success', 'Interno deletado com sucesso!')
                self.load_internos()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, selecione um interno para deletar.')

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
