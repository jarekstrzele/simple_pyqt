# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Drugi_project_znowu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(778, 401)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 9, 781, 381))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lyt_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.lyt_main.setContentsMargins(0, 0, 0, 0)
        self.lyt_main.setObjectName("lyt_main")
        self.gbxCheckable = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gbxCheckable.setCheckable(True)
        self.gbxCheckable.setObjectName("gbxCheckable")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.gbxCheckable)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.rbtCheckTrue = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtCheckTrue.setChecked(True)
        self.rbtCheckTrue.setObjectName("rbtCheckTrue")
        self.verticalLayout.addWidget(self.rbtCheckTrue, 0, QtCore.Qt.AlignHCenter)
        self.rbtCheckFalse = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.rbtCheckFalse.setObjectName("rbtCheckFalse")
        self.verticalLayout.addWidget(self.rbtCheckFalse, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lyt_main.addWidget(self.gbxCheckable)
        self.gbxFlat = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gbxFlat.setFlat(True)
        self.gbxFlat.setObjectName("gbxFlat")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.gbxFlat)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(19, 29, 231, 331))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.rbtFlatTrue = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtFlatTrue.setChecked(True)
        self.rbtFlatTrue.setObjectName("rbtFlatTrue")
        self.verticalLayout_2.addWidget(self.rbtFlatTrue, 0, QtCore.Qt.AlignHCenter)
        self.rbtFlatFalse = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbtFlatFalse.setObjectName("rbtFlatFalse")
        self.verticalLayout_2.addWidget(self.rbtFlatFalse, 0, QtCore.Qt.AlignHCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.lyt_main.addWidget(self.gbxFlat)
        self.gbxAlignment = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.gbxAlignment.setObjectName("gbxAlignment")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.gbxAlignment)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(19, 19, 221, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.rgbAlignLeft = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.rgbAlignLeft.setChecked(True)
        self.rgbAlignLeft.setObjectName("rgbAlignLeft")
        self.verticalLayout_3.addWidget(self.rgbAlignLeft, 0, QtCore.Qt.AlignHCenter)
        self.rbtAlignCenter = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.rbtAlignCenter.setObjectName("rbtAlignCenter")
        self.verticalLayout_3.addWidget(self.rbtAlignCenter, 0, QtCore.Qt.AlignHCenter)
        self.rbtAlignRight = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.rbtAlignRight.setObjectName("rbtAlignRight")
        self.verticalLayout_3.addWidget(self.rbtAlignRight, 0, QtCore.Qt.AlignHCenter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.lyt_main.addWidget(self.gbxAlignment)

        self.retranslateUi(Dialog)
        self.rbtCheckTrue.toggled['bool'].connect(self.gbxCheckable.setChecked) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.rbtCheckTrue.toggled.connect(self.evt_rbtCheckTrue_toggled)
        self.rbtFlatTrue.toggled.connect(self.evt_rbtFlatTrue_toggled)

    def evt_rbtCheckTrue_toggled(self, chk):
        self.gbxCheckable.setCheckable(chk)

    def evt_rbtFlatTrue_toggled(self, chk):
        self.gbxFlat.setFlat(chk)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.gbxCheckable.setTitle(_translate("Dialog", "Checkable"))
        self.rbtCheckTrue.setText(_translate("Dialog", "True"))
        self.rbtCheckFalse.setText(_translate("Dialog", "False"))
        self.gbxFlat.setTitle(_translate("Dialog", "Flat"))
        self.rbtFlatTrue.setText(_translate("Dialog", "True"))
        self.rbtFlatFalse.setText(_translate("Dialog", "False"))
        self.gbxAlignment.setTitle(_translate("Dialog", "Left"))
        self.rgbAlignLeft.setText(_translate("Dialog", "Align Left"))
        self.rbtAlignCenter.setText(_translate("Dialog", "Align Center"))
        self.rbtAlignRight.setText(_translate("Dialog", "Align Right"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
