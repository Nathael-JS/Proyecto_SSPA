from ui_mainparticulas import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from particulas import Particula
from listaparticulas import ListaParticulas
from PySide2.QtCore import Slot


class MainWindow (QMainWindow):
    def __init__(self):
        super (MainWindow, self).__init__()
        self.particula = ListaParticulas()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.AgreFin_pushButton_2.clicked.connect(self.boton_agregarFinal)
        self.ui.AgreIni_pushButton.clicked.connect(self.boton_agregarInicio)
        self.ui.Mostrar_pushButton_3.clicked.connect(self.mostrar)
        
        self.ui.actAbrir.triggered.connect(self.abrir)
        self.ui.actionGuardar.triggered.connect(self.guardar)
        
    def guardar(self):
            ubicacion = QFileDialog.getSaveFileName(
                self,
                'Guardar Archivo',
                '.',
                'JSON (*.json)'
            )
            print (ubicacion[0])
            if self.particula.guardar (ubicacion[0]):
                QMessageBox.information(self,"Se guardo correctamente en "+ ubicacion[0])
            else:
                QMessageBox.warning(self,"Error","No se pudo guardar")
    
    def abrir (self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]

        print(ubicacion)
        if self.particula.abrir(ubicacion):
            QMessageBox.information(self,"Exito","Se cargo correctamente en "+ ubicacion)
        else:
            QMessageBox.warning(self,"Error","No se pudo Abrir")
               
    def boton_agregarFinal (self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.x1_spinBox_2.value()
        destino_x = self.ui.x2_spinBox.value()
        origen_y = self.ui.y1_spinBox_3.value()
        destino_y = self.ui.y2_spinBox_4.value()
        velocidad = self.ui.velocidad_spinBox_5.value()
        red = self.ui.rojo_doubleSpinBox.value()
        blue = self.ui.azul_doubleSpinBox_2.value()
        green = self.ui.verde_doubleSpinBox_3.value()
        
        self.particula.agregar_final(Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,blue,green))
        
    def boton_agregarInicio (self):
        id = self.ui.id_lineEdit.text()
        origen_x = self.ui.x1_spinBox_2.value()
        destino_x = self.ui.x2_spinBox.value()
        origen_y = self.ui.y1_spinBox_3.value()
        destino_y = self.ui.y2_spinBox_4.value()
        velocidad = self.ui.velocidad_spinBox_5.value()
        red = self.ui.rojo_doubleSpinBox.value()
        blue = self.ui.azul_doubleSpinBox_2.value()
        green = self.ui.verde_doubleSpinBox_3.value()
        
        self.particula.agregar_final(Particula(id,origen_x,origen_y,destino_x,destino_y,velocidad,red,blue,green))
        
    def mostrar (self):
        self.ui.salida_plainTextEdit.clear()
        self.ui.salida_plainTextEdit.insertPlainText(str(self.particula))
        
        