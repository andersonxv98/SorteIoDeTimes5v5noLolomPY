from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import  *
import sys
import Teste
from Teste import  Sorteia_praMIM_Percival

class MainWindow(QMainWindow):
    def __init__(self):
        vectorWidget = []
        super().__init__()
        self.setWindowTitle("Sorteio DE Mamaco NO LOL CANSADO")
        self.label = QLabel("Nomes")


        self.jogador1 = QLineEdit()
        self.jogador1.setText("jogador1")

        self.jogador2 = QLineEdit()
        self.jogador2.setText("jogador2")
        self.jogador3 = QLineEdit()
        self.jogador3.setText("jogador3")
        self.jogador4 = QLineEdit()
        self.jogador4.setText("jogador4")
        self.jogador5 = QLineEdit()
        self.jogador5.setText("jogador5")
        self.jogador6 = QLineEdit()
        self.jogador6.setText("jogador6")
        self.jogador7 = QLineEdit()
        self.jogador7.setText("jogador7")
        self.jogador8 = QLineEdit()
        self.jogador8.setText("jogador8")
        self.jogador9 = QLineEdit()
        self.jogador9.setText("jogador9")
        self.jogador10 = QLineEdit()
        self.jogador10.setText("jogador10")

        layout= QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.jogador1)
        layout.addWidget(self.jogador2)
        layout.addWidget(self.jogador3)
        layout.addWidget(self.jogador4)
        layout.addWidget(self.jogador5)
        layout.addWidget(self.jogador6)
        layout.addWidget(self.jogador7)
        layout.addWidget(self.jogador8)
        layout.addWidget(self.jogador9)
        layout.addWidget(self.jogador10)

        self.button = QPushButton("Sortear OS MAMACOS")
        self.button.clicked.connect(self.Chama_outra_class)
        layout.addWidget(self.button)

        self.time1_lb = QLabel("TIME 1")
        self.time2_lb = QLabel("TIME 2")
        layout.addWidget(self.time1_lb)
        layout.addWidget(self.time2_lb)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def Add_resultado_sorteio(self, result1, result2):
        print("Entrou ADD_resuldado_sorteio")
        print("TIME 1 DENTRO DA VIEW CONCOLES: ", result1)
        print("TIME 1 DENTRO DA VIEW CONCOLES: ", result2)
        novo_label1 = QLabel("teste1")
        novo_label2 = QLabel("teste2")
        team1 = "time 1: "
        team2 = "time 2: "
        for x in result1:
            team1 += " , "+x
        for y in result2:
            team2 += " , "+y

        self.time1_lb.setText(team1)
        self.time2_lb.setText(team2)

    def Chama_outra_class(self):
        print("Entrou na func Chama_outra_class")
        var1  = self.jogador1.text()
        var2 = self.jogador2.text()
        var3 = self.jogador3.text()
        var4 = self.jogador4.text()
        var5 = self.jogador5.text()
        var6 = self.jogador6.text()
        var7 = self.jogador7.text()
        var8 = self.jogador8.text()
        var9 = self.jogador9.text()
        var10 = self.jogador10.text()
        time1, time2 = Sorteia_praMIM_Percival(var1 ,var2, var3, var4,var5, var6, var7, var8, var9, var10)

        self.Add_resultado_sorteio(time1, time2)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()