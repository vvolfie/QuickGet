# Form implementation generated from reading ui file 'C:\Users\Álvaro\Desktop\utili_instalar\sobre.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form_2(object):
    def setupUi(self, Form_2):
        Form_2.setObjectName("Form_2")
        Form_2.resize(301, 208)
        Form_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 301, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.about_titulo = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.about_titulo.setMaximumSize(QtCore.QSize(300, 200))
        font = QtGui.QFont()
        font.setFamily("Roman")
        font.setPointSize(9)
        font.setBold(True)
        self.about_titulo.setFont(font)
        self.about_titulo.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.about_titulo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.about_titulo.setObjectName("about_titulo")
        self.verticalLayout.addWidget(self.about_titulo)
        self.about_text = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.about_text.setMaximumSize(QtCore.QSize(300, 200))
        self.about_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.about_text.setObjectName("about_text")
        self.verticalLayout.addWidget(self.about_text)
        self.button_sobre_ok = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.button_sobre_ok.setMinimumSize(QtCore.QSize(0, 0))
        self.button_sobre_ok.setMaximumSize(QtCore.QSize(60, 30))
        self.button_sobre_ok.setObjectName("button_sobre_ok")
        self.verticalLayout.addWidget(self.button_sobre_ok, 0, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.retranslateUi(Form_2)
        QtCore.QMetaObject.connectSlotsByName(Form_2)

    def retranslateUi(self, Form_2):
        _translate = QtCore.QCoreApplication.translate
        Form_2.setWindowTitle(_translate("Form_2", "Form"))
        self.about_titulo.setText(_translate("Form_2", "SOBRE"))
        self.about_text.setText(_translate("Form_2", "TextLabel"))
        self.button_sobre_ok.setText(_translate("Form_2", "OK"))
