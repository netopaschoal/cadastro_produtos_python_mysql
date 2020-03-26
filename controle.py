from PyQt5 import  uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    if formulario.radioButton.isChecked() :
        print("Categoria Eletronicos selecionada")
    elif formulario.radioButton_2.isChecked() :
        print("Categoria Informatica selecionada")
    else :
        print("Categoria Alimentos selecionada")

    print("Código:",linha1)
    print("Descricao:",linha2)
    print("Preco",linha3)
    

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario2.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()