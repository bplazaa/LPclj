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
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
#from PyQt5.QtGui import QAp

from lexico import verLexer
from sintactico import verParser

class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.window = QWidget(self)
        self.setWindowTitle("Proyecto Clojure 1")
        self.window.setGeometry(100, 75, 600, 450)
        self.layout = QGridLayout(self)
        self.line = QPlainTextEdit(self)
        self.viewLex = QPlainTextEdit(self)
        self.viewPar = QPlainTextEdit(self)
        self.button = QPushButton("Limpiar")

        self.button1= QPushButton("Ver Lexer")
        self.button2= QPushButton("Ver Parser")
        self.button3= QPushButton("Lexer + Parser")
        self.button1.clicked.connect(self.clickMethodLexer)
        self.button2.clicked.connect(self.clickMethodParser)
        self.button3.clicked.connect(self.clickMethodFull)
        self.panelV= QVBoxLayout(self)
        self.panelV.addWidget(self.button1)
        self.panelV.addWidget(self.button2)
        self.panelV.addWidget(self.button3)

        self.label = QLabel("\t\t     Somos el Grupo Clojure 1\n \t\t\t Bienvenidos\n\n")

        self.label.setFont(QFont("Times", 16, QFont.Bold))

        self.tokens = QHBoxLayout(self)
        self.tokens.addWidget(self.viewLex)
        self.tokens.addWidget(self.viewPar)



        self.button.clicked.connect(self.clickMethodLimpiar)
        #self.view.setReadOnly(True)
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.line, 1, 0)
        self.layout.addWidget(self.button, 1, 1)
        self.layout.addLayout(self.panelV,2,1)
        self.layout.addLayout(self.tokens,2,0)
        self.button.resize(200, 32)
        self.window.setLayout(self.layout)


    def clickMethodLexer(self):  # ver lexer
        self.viewLex.clear()
        self.viewLex.insertPlainText("Tokens del Lexico\n*******")
        self.viewLex.insertPlainText(verLexer(self.line.toPlainText()))

    def clickMethodParser(self):  # ver parser
        self.viewPar.clear()
        self.viewPar.insertPlainText("Reglas de Parsing\n*******")
        mensaje = verLexer(self.line.toPlainText())
        if(mensaje.__contains__("no reconocido")):
            self.viewPar.insertPlainText("\n Error en el lexico, no es posible continuar.")
        else:
            self.viewPar.insertPlainText(verParser(self.line.toPlainText()))
        
    
    def clickMethodFull(self):  # ver lexer
        self.clickMethodLexer()
        self.clickMethodParser()

    def clickMethodLimpiar(self):#borrar
        self.line.clear()
        self.viewLex.clear()
        self.viewPar.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    mainWin.resize(800, 600)
    sys.exit( app.exec_() )