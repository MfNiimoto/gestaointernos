# main.py

from calendar import c
from json import load
import sys
import sqlite3
from datetime import datetime
from turtle import setworldcoordinates
from PySide6.QtWidgets import QApplication, QWidget, QColorDialog, QMessageBox, QTreeWidgetItem, QFileDialog, QDialog, QVBoxLayout, QLabel, QPushButton
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtCore import QPoint
from form import Ui_Widget
from exibTrab import Ui_Form_Trab
from exibAtend import Ui_Form_Atend
from PySide6.QtGui import QColor, QPixmap

class MainWindow(QWidget):
    def __init__(self): # inicializa a interface gráfica
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
        self.ui.pbEntradaAud.clicked.connect(self.save_video)
        self.ui.btnSaidaAud.clicked.connect(self.delete_video)
        self.ui.btnEntAtend.clicked.connect(self.save_atendimento)
        self.ui.btnSaiAtend.clicked.connect(self.delete_atendimento)
        self.ui.txtBarCodeExib.returnPressed.connect(self.ent_barcode)
        self.set_setor()
        self.hideTab()
        self.hide_frame_setor()
        self.load_video()
        self.load_setores()
        self.load_internos()
        self.load_atendimento()
        
    def create_tables(self): # cria as tabelas do banco de dados
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
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS video (
                                id INTEGER PRIMARY KEY,
                                nome_video TEXT NOT NULL,
                                cela_video TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS atendimento (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                cela TEXT NOT NULL,
                                setor TEXT NOT NULL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
                                id INTEGER PRIMARY KEY,
                                nome TEXT NOT NULL,
                                saida DATETIME2,
                                entrada DATETIME2)''')

        self.connection.commit()

    def hideTab(self):
        self.ui.tabRelatorio.hide()
    

    def choose_color(self, event): # escolhe a cor do setor
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.lblCor.setStyleSheet(f'background-color: {color.name()}')
            self.ui.lblCor.setText(color.name())

    def save_setor(self): # salva o setor
        nome = self.ui.txtSetorCadastro.text().upper()
        cor = self.ui.lblCor.text().upper()
        if nome and cor:
            self.cursor.execute('INSERT INTO setores (nome, cor) VALUES (?, ?)', (nome, cor))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Setor cadastrado com sucesso!')
            self.load_setores()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, preencha todos os campos.')

    def load_setores(self): # carrega os setores da tabela setores no widget tree
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

    def delete_setor(self): # exclui o setor
        selected_item = self.ui.treeSetores.currentItem()
        if selected_item:
            nome = selected_item.text(0)
            self.cursor.execute('DELETE FROM setores WHERE nome = ?', (nome,))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Setor deletado com sucesso!')
            self.load_setores()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, selecione um setor para deletar.')

    def select_photo(self): # seleciona a foto do interno
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Photo", "", "Images (*.png *.xpm *.jpg)", options=options)
        if file_name:
            self.ui.tbFoto.setText(file_name)

    def save_interno(self): # salva o interno
        nome = self.ui.txtNome.text().upper()  
        rgi = self.ui.txtRGI.text().upper()
        cela = self.ui.txtCela.text().upper()
        barcode = self.ui.txtBarCode.text().upper()
        setor = self.ui.cbbSetor.currentText().upper()
        foto = self.ui.tbFoto.text()
        if nome and rgi and cela and barcode and setor:    # verifica se todos os campos estão preenchidos
            self.cursor.execute('INSERT INTO internos (nome, rgi, cela, barcode, setor, foto) VALUES (?, ?, ?, ?, ?, ?)', (nome, rgi, cela, barcode, setor, foto)) # insere os dados na tabela internos
            self.connection.commit() 
            QMessageBox.information(self, 'Success', 'Interno cadastrado com sucesso!')
            self.load_internos()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, preencha todos os campos.')

    def load_internos(self): # carrega os internos da tabela internos no widget tree
        self.ui.treeInternos.clear()
        self.cursor.execute('SELECT nome, rgi, setor, cela FROM internos')
        internos = self.cursor.fetchall()
        for interno in internos:
            item = QTreeWidgetItem([interno[0], interno[1], interno[2], interno[3]]) # cria item com os dados da tabela internos
            self.ui.treeInternos.addTopLevelItem(item) # adiciona o item ao widget tree
 
    def hide_frame_setor(self): # esconde todos os frames de setores
        self.ui.frame_setor_1.hide()
        self.ui.frame_setor_2.hide()
        self.ui.frame_setor_3.hide()
        self.ui.frame_setor_4.hide()
        self.ui.frame_setor_5.hide()
        self.ui.frame_setor_6.hide()
        self.ui.frame_setor_7.hide()
        self.ui.frame_setor_8.hide()
        self.ui.frame_setor_9.hide()
        self.ui.frame_setor_10.hide()
        self.ui.frame_setor_11.hide()
        self.ui.frame_setor_12.hide()
        self.ui.frame_setor_13.hide()
        self.ui.frame_setor_14.hide()
        self.ui.frame_setor_15.hide()
        self.ui.frame_setor_16.hide()
        self.ui.frame_setor_17.hide()
        self.ui.frame_setor_18.hide()
        self.ui.frame_setor_19.hide()
        self.ui.frame_setor_20.hide()   

    def set_setor(self): # seta o frame_setor correto para exibir o nome do setor
        self.cursor.execute('SELECT nome, cor FROM setores')
        setores = self.cursor.fetchall()
        for i, (nome,cor) in enumerate(setores):
            while i < 20:
                frame = getattr(self.ui,f'frame_setor_{i+1}')
                label = getattr(self.ui,f'label_setor_{i+1}')                
                label.setText(nome)
                i== i+1
                break
                
    def set_setor_cor(self, setor, i): # verifica a cor do setor e seta a cor do label
        self.cursor.execute('SELECT cor FROM setores WHERE nome = ?', (setor,))
        cor = self.cursor.fetchone()
        if cor:
            label = getattr(self.ui,f'label_setor_{i+1}')
            label.setStyleSheet(f'background-color: {cor[0]}')
  
    def ent_barcode(self): 
        barcode = self.ui.txtBarCodeExib.text()
        self.cursor.execute('SELECT nome, cela, setor FROM internos WHERE barcode = ?', (barcode,))
        interno = self.cursor.fetchone()

        if interno:
            nome = interno[0]
            cela = interno[1]
            setor = interno[2]
            
            # Variáveis para controlar o estado
            found = False
            tree_setor_alocado = None

            # Passo 1: Verifica se o interno já está em alguma TreeView
            for i in range(20):
                tree_setor = getattr(self.ui, f'tw_setor_{i+1}')
                frame_setor = getattr(self.ui, f'frame_setor_{i+1}')
                
                top_level_count = tree_setor.topLevelItemCount()
                
                for j in range(top_level_count):
                    item = tree_setor.topLevelItem(j)
                    if item.text(0) == nome:  # Interno já está na TreeView
                        tree_setor.takeTopLevelItem(j)  # Remove o interno
                        if tree_setor.topLevelItemCount() == 0:
                            frame_setor.hide()  # Oculta a TreeView se estiver vazia
                        self.ui.txtBarCodeExib.clear()
                        self.registro_saida(barcode)
                        return  # Termina a função porque o interno foi removido
            
            # Passo 2: Verifica se já existe uma TreeView exibida com o setor correspondente
            for i in range(20):
                tree_setor = getattr(self.ui, f'tw_setor_{i+1}')
                frame_setor = getattr(self.ui, f'frame_setor_{i+1}')
                txt_setor = getattr(self.ui, f'label_setor_{i+1}')
                
                if frame_setor.isVisible():  # Se a TreeView está visível
                    if txt_setor.text() == setor:  # Se é o setor correspondente
                        tree_setor_alocado = tree_setor
                        break
            
            # Passo 3: Se não encontrar uma TreeView correspondente, busca a primeira disponível
            if not tree_setor_alocado:
                for i in range(20):
                    tree_setor = getattr(self.ui, f'tw_setor_{i+1}')
                    frame_setor = getattr(self.ui, f'frame_setor_{i+1}')
                    
                    if not frame_setor.isVisible():  # Encontrou a primeira TreeView disponível
                        tree_setor_alocado = tree_setor
                        txt_setor = getattr(self.ui, f'label_setor_{i+1}')
                        txt_setor.setText(setor)  # Configura o setor no label
                        self.set_setor_cor(setor, i) # seta a cor do setor
                        frame_setor.show()
                        break

            # Passo 4: Adiciona o interno na TreeView encontrada ou alocada
            if tree_setor_alocado:
                tree_setor_alocado.addTopLevelItem(QTreeWidgetItem([nome, cela]))
                tree_setor_alocado.setCurrentItem(tree_setor_alocado.topLevelItem(0))
                self.ui.txtBarCodeExib.clear()
                self.registro_entrada(barcode)

        else:
            QMessageBox.warning(self, 'Warning', 'Código de barras inválido.')

    def registro_entrada(self, barcode): # registra a entrada do interno
        self.cursor.execute('SELECT nome FROM internos WHERE barcode = ?', (barcode,)) # verifica se o interno já foi cadastrado
        interno = self.cursor.fetchone() # verifica se o interno já foi cadastrado
        if interno: 
            nome = interno[0] # nome do interno
            data_entrada = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # data e hora de entrada
            self.cursor.execute('INSERT INTO registros (nome, entrada) VALUES (?, ?)', (nome, data_entrada))
            self.connection.commit()    # registra a entrada do interno

    def registro_saida(self, barcode): # registra a saída do interno
        self.cursor.execute('SELECT nome FROM internos WHERE barcode = ?', (barcode,)) # verifica se o interno já foi cadastrado
        interno = self.cursor.fetchone()
        if interno:
            nome = interno[0]
            data_saida = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # data e hora de saída
            self.cursor.execute('UPDATE registros SET saida = ? WHERE nome = ? AND saida IS NULL', (data_saida, nome))
            self.connection.commit()

    def show_interno_details(self, item): # exibe os detalhes do interno selecionado
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

    def delete_interno(self): # exclui o interno
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

      # controle de vídeo audiencia

    def save_video(self): # salva o vídeo audiencia
        nome_video = self.ui.txtNomeAud.text().upper()
        cela_video = self.ui.txtCelaAud.text().upper()
        if nome_video and cela_video:
            self.cursor.execute('INSERT INTO video (nome_video, cela_video) VALUES (?, ?)', (nome_video, cela_video))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Vídeo cadastrado com sucesso!')
            self.load_video()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, preencha todos os campos.')

    def load_video(self): # exibe todas as entradas de vídeo no widget tree com as colunas nome e cela
        self.ui.twAudiencia.clear() # limpa o widget tree
        self.cursor.execute('SELECT nome_video, cela_video FROM video') # seleciona todas as entradas de vídeo
        video = self.cursor.fetchall() # armazena em uma lista
        for v in video: # percorre a lista e adiciona cada entrada como uma linha no widget tree
            item = QTreeWidgetItem([v[0], v[1]])
            self.ui.twAudiencia.addTopLevelItem(item)
    
    def delete_video(self): # exclui o vídeo audiencia
        selected_item = self.ui.twAudiencia.currentItem()
        if selected_item:
            nome_video = selected_item.text(0)
            reply = QMessageBox.question(self, 'Confirmar Exclusão', f'Tem certeza que deseja excluir o vídeo {nome_video}?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cursor.execute('DELETE FROM video WHERE nome_video = ?', (nome_video,))
                self.connection.commit()
                QMessageBox.information(self, 'Success', 'Vídeo deletado com sucesso!')
                self.load_video()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, selecione um vídeo para deletar.')

    def save_atendimento(self): # salva o atendimento
        nome = self.ui.txtNomeAtend.text().upper() # seleciona o nome do atendimento
        cela = self.ui.txtCelaAtend.text().upper() # seleciona a cela do atendimento
        setor = self.ui.cbbAtend.currentText().upper() # seleciona o setor do atendimento
        if nome and cela and setor: 
            self.cursor.execute('INSERT INTO atendimento (nome, cela, setor) VALUES (?, ?, ?)', (nome, cela, setor))
            self.connection.commit()
            QMessageBox.information(self, 'Success', 'Atendimento cadastrado com sucesso!')
            self.load_atendimento()
    
    def load_atendimento(self): # carrega os atendimentos da tabela atendimento no widget tree
        self.ui.treeAtendimento.clear()
        self.cursor.execute('SELECT nome, cela, setor FROM atendimento')
        atendimento = self.cursor.fetchall()
        for atend in atendimento:
            item = QTreeWidgetItem([atend[0], atend[1], atend[2]])
            self.ui.treeAtendimento.addTopLevelItem(item)

    def delete_atendimento(self): # exclui o atendimento

        selected_item = self.ui.treeAtendimento.currentItem()
        if selected_item:
            nome = selected_item.text(0)
            reply = QMessageBox.question(self, 'Confirmar Exclusão', f'Tem certeza que deseja excluir o atendimento {nome}?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cursor.execute('DELETE FROM atendimento WHERE nome = ?', (nome,))
                self.connection.commit()
                QMessageBox.information(self, 'Success', 'Atendimento deletado com sucesso!')
                self.load_atendimento()
        else:
            QMessageBox.warning(self, 'Warning', 'Por favor, selecione um atendimento para deletar.')
        #fim da parte de controle de atendimento

    def closeEvent(self, event): # fecha a conexão com o banco de dados
        self.connection.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
