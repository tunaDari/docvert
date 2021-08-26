# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from .custom_widgets import FileList

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(857, 551)
        Form.setStyleSheet("background-color: rgb(245, 220, 255);")
        self.setWindowIcon(QtGui.QIcon(":/logo/docvert.png"))
        self.setWindowTitle("Docvert")
        self.setFixedSize(self.size())
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputList = FileList(Form)
        self.inputList.setAcceptDrops(True)
        self.inputList.setStyleSheet("QListWidget{\n"
"    border: 2px solid rgb(186, 129, 255);\n"
"    background-image: url(drop_icon.png);\n"
"    background-position: center;\n"
"}\n"
"")
        self.inputList.setObjectName("inputList")
        self.horizontalLayout.addWidget(self.inputList)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.convertBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.convertBtn.setFont(font)
        self.convertBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(104, 48, 127);\n"
"    color: white;\n"
"    border-radius:10px;\n"
"    padding:6px\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(177, 82, 217);\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"       background-color:rgb(235, 169, 235);\n"
"}")
        self.convertBtn.setObjectName("convertBtn")
        self.verticalLayout.addWidget(self.convertBtn)
        
        self.cancelBtn = QtWidgets.QPushButton(Form)
        self.cancelBtn.setVisible(True)
        self.cancelBtn.setText("Cancel")
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(104, 48, 127);\n"
"    color: white;\n"
"    border-radius:10px;\n"
"    padding:6px\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(177, 82, 217);\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"       background-color:rgb(235, 169, 235);\n"
"}")
        self.cancelBtn.setObjectName("cancelBtn") 
        self.verticalLayout.addWidget(self.cancelBtn)
        
        self.clearAllBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.clearAllBtn.setFont(font)
        self.clearAllBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(104, 48, 127);\n"
"    color: white;\n"
"    border-radius:10px;\n"
"    padding:6px\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(177, 82, 217);\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"       background-color:rgb(235, 169, 235);\n"
"}")
        self.clearAllBtn.setObjectName("clearAllBtn")
        self.verticalLayout.addWidget(self.clearAllBtn)
        self.mergeBtn = QtWidgets.QPushButton(Form)
        self.mergeBtn.setText("Merge")
        self.mergeBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(104, 48, 127);\n"
"    color: white;\n"
"    border-radius:10px;\n"
"    padding:6px\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(177, 82, 217);\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"       background-color:rgb(235, 169, 235);\n"
"}")
        self.mergeBtn.setFont(font)
        self.verticalLayout.addWidget(self.mergeBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.outputList = FileList(Form)
        self.outputList.setAcceptDrops(False)
        self.outputList.setStyleSheet("QListWidget{\n"
"    border: 2px solid rgb(186, 129, 255);\n"
"}\n"
"")
        self.outputList.setObjectName("outputList")
        self.horizontalLayout.addWidget(self.outputList)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.statusLabel = QtWidgets.QLabel(Form)
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setObjectName("statusLabel")
        self.gridLayout.addWidget(self.statusLabel, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, -1, 13, 7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.WORDtoPDF = QtWidgets.QRadioButton(Form)
        self.WORDtoPDF.setStyleSheet("QRadioButton::indicator {\n"
"height: 14px;\n"
"width: 14px;\n"
"border-style:solid;\n"
"border-radius:7px;\n"
"border-width: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #48a5fd;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #68307f, stop:1 #68307f);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    border-color: #a9b7c6;\n"
"    background-color: #fbfdfa;\n"
"}")
        self.WORDtoPDF.setObjectName("WORDtoPDF")
        self.WORDtoPDF.setChecked(True)
        self.verticalLayout_6.addWidget(self.WORDtoPDF)
        self.PPTtoPDF = QtWidgets.QRadioButton(Form)
        self.PPTtoPDF.setStyleSheet("QRadioButton::indicator {\n"
"height: 14px;\n"
"width: 14px;\n"
"border-style:solid;\n"
"border-radius:7px;\n"
"border-width: 1px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    border-color: #48a5fd;\n"
"    background-color: qradialgradient(cx:0.5, cy:0.5, radius:0.4,fx:0.5, fy:0.5, stop:0 #ffffff, stop:0.5 #ffffff, stop:0.6 #68307f, stop:1 #68307f);\n"
"}\n"
"QRadioButton::indicator:!checked {\n"
"    border-color: #a9b7c6;\n"
"    background-color: #fbfdfa;\n"
"}")
        self.PPTtoPDF.setObjectName("PPTtoPDF")
        self.verticalLayout_6.addWidget(self.PPTtoPDF)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, -1, 11, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mergeCB = QtWidgets.QCheckBox(Form)
        self.mergeCB.setStyleSheet("QPushButton{\n"
"    background-color: rgb(104, 48, 127);\n"
"    color: white;\n"
"    border-radius:10px;\n"
"    padding:6px\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(177, 82, 217);\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"       background-color:rgb(235, 169, 235);\n"
"}")
        self.mergeCB.setObjectName("mergeCB")
        self.verticalLayout_2.addWidget(self.mergeCB)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.saveFolderEdit = QtWidgets.QLineEdit(Form)
        self.saveFolderEdit.setReadOnly(True)
        self.saveFolderEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.saveFolderEdit.setObjectName("saveFolderEdit")
        self.horizontalLayout_2.addWidget(self.saveFolderEdit)
        self.saveFolderBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.saveFolderBtn.setFont(font)
        self.saveFolderBtn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(104, 48, 127);\n"
"    color: white;\n"
"    border-radius:10px;\n"
"    padding:6px\n"
"}\n"
"\n"
"QPushButton#pushButton:hover {\n"
"    background-color: rgb(177, 82, 217);\n"
"    color: white\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"       background-color:rgb(235, 169, 235);\n"
"}")
        self.saveFolderBtn.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.saveFolderBtn)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"    background-color: rgb(186, 129, 255);\n"
"    border: solid grey;\n"
"    border-radius: 10px;\n"
"    color: white;\n"
"    font: 8pt \"Segoe UI\";\n"
"    text-align: center\n"
"}\n"
"\n"
"QProgressBar::chunk \n"
"{\n"
"    background-color: rgb(104, 48, 127);\n"
"    border-radius :10px;\n"
"}      ")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(17, 20, 66);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(17, 20, 66);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setIndent(34)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Docvert", "Docvert"))
        self.convertBtn.setText(_translate("Form", "Convert"))
        self.clearAllBtn.setText(_translate("Form", "Clear"))
        self.statusLabel.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "Conversion Type"))
        self.WORDtoPDF.setText(_translate("Form", "WORD to PDF"))
        self.PPTtoPDF.setText(_translate("Form", "PPT to PDF"))
        self.mergeCB.setText(_translate("Form", "Merge output files"))
        self.saveFolderBtn.setText(_translate("Form", "Save Location"))
        self.label.setText(_translate("Form", "Files to convert"))
        self.label_2.setText(_translate("Form", "Converted Files"))