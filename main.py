# main.py

import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QColorDialog, QMessageBox, QTreeWidgetItem
from form import Ui_Widget
from PySide6.QtGui import QColor

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.connection = sqlite3.connect('controle.db')
        self.cursor = self.connection.cursor()
        self.create_table()
        self.ui.lblCor.mousePressEvent = self.choose_color
        self.ui.btnSalvarSetor.clicked.connect(self.save_setor)
        self.ui.btnAtualizarSetor.clicked.connect(self.load_setores)
        self.ui.btnDeletarCadastro.clicked.connect(self.delete_setor)
        self.load_setores()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS setores (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                cor TEXT NOT NULL)''')
        self.connection.commit()

    def choose_color(self, event):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.lblCor.setStyleSheet(f'background-color: {color.name()}')
            self.ui.lblCor.setText(color.name())

    def save_setor(self):
        nome = self.ui.txtSetorCadastro.text()
        cor = self.ui.lblCor.text()
        if nome and cor:
            self.cursor.execute('INSERT INTO setores (nome, cor) VALUES (?, ?)', (nome, cor))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Setor cadastrado com sucesso!')
            self.load_setores()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, preencha todos os campos.')

    def load_setores(self):
        self.ui.treeSetores.clear()
        self.cursor.execute('SELECT nome, cor FROM setores')
        setores = self.cursor.fetchall()
        for setor in setores:
            item = QTreeWidgetItem([setor[0], setor[1]])
            item.setBackground(0, QColor(setor[1]))
            item.setBackground(1, QColor(setor[1]))
            self.ui.treeSetores.addTopLevelItem(item)

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

    def closeEvent(self, event):
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
