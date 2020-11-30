import sys
#IMPORTAR componenetes necesarios
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QVBoxLayout
#from PyQt5.QtGui import QAp

from lexico import verLexer
from sintactico import verParser

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.window = QWidget(self)
        self.setWindowTitle("Proyecto Grupo 1")
        self.window.setGeometry(100, 75, 400, 280)
        self.layout = QGridLayout(self)
        self.line = QPlainTextEdit(self)
        self.view = QPlainTextEdit(self)
        self.button = QPushButton("Limpiar")

        self.button1= QPushButton("Ver Lexer")
        self.button2= QPushButton("Ver Parser")
        self.button1.clicked.connect(self.clickMethodLexer)
        self.button2.clicked.connect(self.clickMethodParser)
        self.panelV= QVBoxLayout(self)
        self.panelV.addWidget(self.button1)
        self.panelV.addWidget(self.button2)

        self.label = QLabel("Somos el Grupo 1\n Bienvenidos")

        self.button.clicked.connect(self.clickMethodLimpiar)
        #self.view.setReadOnly(True)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.line, 1, 0)
        self.layout.addWidget(self.button, 1, 1)
        self.layout.addLayout(self.panelV,2,1)
        self.layout.addWidget(self.view, 2, 0)
        self.button.resize(200, 32)
        self.window.setLayout(self.layout)

    def clickMethod(self):#inserta palabra  copia
        self.view.insertPlainText(self.line.toPlainText()+"\n")

    def clickMethodLexer(self):  # ver lexer
        self.view.setPlainText(verLexer(self.line.toPlainText()))

    def clickMethodParser(self):  # ver parser
        self.view.insertPlainText(verParser(self.line.toPlainText()))

    def clickMethodLimpiar(self):#borrar
        self.view.insertPlainText(self.line.clear())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    mainWin.resize(600, 500)
    sys.exit( app.exec_() )