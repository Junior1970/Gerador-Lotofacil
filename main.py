import random
from PyQt5 import uic,QtWidgets


def sortear():
    numeros = ["01","02","03","04","05","06","07","08","09",10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

    random.shuffle(numeros)


    tela.num_1.setText(str(numeros[0]))
    tela.num_2.setText(str(numeros[1]))
    tela.num_3.setText(str(numeros[2]))
    tela.num_4.setText(str(numeros[3]))
    tela.num_5.setText(str(numeros[4]))
    tela.num_6.setText(str(numeros[5]))
    tela.num_7.setText(str(numeros[6]))
    tela.num_8.setText(str(numeros[7]))
    tela.num_9.setText(str(numeros[8]))
    tela.num_10.setText(str(numeros[10]))
    tela.num_11.setText(str(numeros[11]))
    tela.num_12.setText(str(numeros[12]))
    tela.num_13.setText(str(numeros[13]))
    tela.num_14.setText(str(numeros[14]))
    tela.num_15.setText(str(numeros[15]))
    

app=QtWidgets.QApplication([])
tela=uic.loadUi("tela_loto.ui") 

tela.pushButton.clicked.connect(sortear)
        

tela.show()
app.exec()
