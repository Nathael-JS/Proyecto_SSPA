# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainParticulas.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(451, 361)
        self.actAbrir = QAction(MainWindow)
        self.actAbrir.setObjectName(u"actAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")

        self.gridLayout_3.addWidget(self.id_lineEdit, 0, 1, 1, 3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 2)

        self.y1_spinBox_3 = QSpinBox(self.groupBox)
        self.y1_spinBox_3.setObjectName(u"y1_spinBox_3")

        self.gridLayout_3.addWidget(self.y1_spinBox_3, 1, 3, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 4, 1, 1)

        self.x1_spinBox_2 = QSpinBox(self.groupBox)
        self.x1_spinBox_2.setObjectName(u"x1_spinBox_2")

        self.gridLayout_3.addWidget(self.x1_spinBox_2, 1, 5, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 2)

        self.y2_spinBox_4 = QSpinBox(self.groupBox)
        self.y2_spinBox_4.setObjectName(u"y2_spinBox_4")

        self.gridLayout_3.addWidget(self.y2_spinBox_4, 2, 3, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 4, 1, 1)

        self.x2_spinBox = QSpinBox(self.groupBox)
        self.x2_spinBox.setObjectName(u"x2_spinBox")

        self.gridLayout_3.addWidget(self.x2_spinBox, 2, 5, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.velocidad_spinBox_5 = QSpinBox(self.groupBox)
        self.velocidad_spinBox_5.setObjectName(u"velocidad_spinBox_5")

        self.gridLayout_3.addWidget(self.velocidad_spinBox_5, 3, 3, 1, 1)

        self.salida_plainTextEdit = QPlainTextEdit(self.groupBox)
        self.salida_plainTextEdit.setObjectName(u"salida_plainTextEdit")

        self.gridLayout_3.addWidget(self.salida_plainTextEdit, 3, 4, 5, 3)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)

        self.rojo_doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.rojo_doubleSpinBox.setObjectName(u"rojo_doubleSpinBox")

        self.gridLayout_3.addWidget(self.rojo_doubleSpinBox, 5, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 6, 0, 1, 1)

        self.azul_doubleSpinBox_2 = QDoubleSpinBox(self.groupBox)
        self.azul_doubleSpinBox_2.setObjectName(u"azul_doubleSpinBox_2")

        self.gridLayout_3.addWidget(self.azul_doubleSpinBox_2, 6, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(28, 0))

        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)

        self.verde_doubleSpinBox_3 = QDoubleSpinBox(self.groupBox)
        self.verde_doubleSpinBox_3.setObjectName(u"verde_doubleSpinBox_3")
        self.verde_doubleSpinBox_3.setValue(30.000000000000000)

        self.gridLayout_3.addWidget(self.verde_doubleSpinBox_3, 7, 2, 1, 1)

        self.AgreIni_pushButton = QPushButton(self.groupBox)
        self.AgreIni_pushButton.setObjectName(u"AgreIni_pushButton")

        self.gridLayout_3.addWidget(self.AgreIni_pushButton, 8, 0, 1, 2)

        self.AgreFin_pushButton_2 = QPushButton(self.groupBox)
        self.AgreFin_pushButton_2.setObjectName(u"AgreFin_pushButton_2")

        self.gridLayout_3.addWidget(self.AgreFin_pushButton_2, 8, 4, 1, 1)

        self.Mostrar_pushButton_3 = QPushButton(self.groupBox)
        self.Mostrar_pushButton_3.setObjectName(u"Mostrar_pushButton_3")

        self.gridLayout_3.addWidget(self.Mostrar_pushButton_3, 8, 6, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tablaP = QTableWidget(self.tab_2)
        self.tablaP.setObjectName(u"tablaP")

        self.gridLayout.addWidget(self.tablaP, 0, 0, 1, 3)

        self.BuscarT_lineEdit = QLineEdit(self.tab_2)
        self.BuscarT_lineEdit.setObjectName(u"BuscarT_lineEdit")

        self.gridLayout.addWidget(self.BuscarT_lineEdit, 1, 0, 1, 1)

        self.BuscarP_pushButton = QPushButton(self.tab_2)
        self.BuscarP_pushButton.setObjectName(u"BuscarP_pushButton")

        self.gridLayout.addWidget(self.BuscarP_pushButton, 1, 1, 1, 1)

        self.MostrarP_pushButton_2 = QPushButton(self.tab_2)
        self.MostrarP_pushButton_2.setObjectName(u"MostrarP_pushButton_2")

        self.gridLayout.addWidget(self.MostrarP_pushButton_2, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 451, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Origen en Y", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen en  X", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Destino en Y", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Destino en  X", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rojo", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Verde", None))
        self.AgreIni_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar al Inicio", None))
        self.AgreFin_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Agregar al Final", None))
        self.Mostrar_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.BuscarT_lineEdit.setText(QCoreApplication.translate("MainWindow", u"Buscar particula...", None))
        self.BuscarP_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.MostrarP_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi
