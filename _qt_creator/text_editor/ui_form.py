# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSet_Dark_Mode = QAction(MainWindow)
        self.actionSet_Dark_Mode.setObjectName(u"actionSet_Dark_Mode")
        self.actionSet_Light_Mode = QAction(MainWindow)
        self.actionSet_Light_Mode.setObjectName(u"actionSet_Light_Mode")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionIncrease_Font_Size = QAction(MainWindow)
        self.actionIncrease_Font_Size.setObjectName(u"actionIncrease_Font_Size")
        self.actionDecrease_Font_Size = QAction(MainWindow)
        self.actionDecrease_Font_Size.setObjectName(u"actionDecrease_Font_Size")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuAppearance = QMenu(self.menubar)
        self.menuAppearance.setObjectName(u"menuAppearance")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuAppearance.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuAppearance.addAction(self.actionSet_Dark_Mode)
        self.menuAppearance.addAction(self.actionSet_Light_Mode)
        self.menuAppearance.addSeparator()
        self.menuAppearance.addSeparator()
        self.menuAppearance.addAction(self.actionIncrease_Font_Size)
        self.menuAppearance.addAction(self.actionDecrease_Font_Size)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S, Return", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionSet_Dark_Mode.setText(QCoreApplication.translate("MainWindow", u"Set Dark Mode", None))
        self.actionSet_Light_Mode.setText(QCoreApplication.translate("MainWindow", u"Set Light Mode", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
#if QT_CONFIG(shortcut)
        self.actionCut.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
#if QT_CONFIG(shortcut)
        self.actionPaste.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+V", None))
#endif // QT_CONFIG(shortcut)
        self.actionIncrease_Font_Size.setText(QCoreApplication.translate("MainWindow", u"Increase Font Size", None))
        self.actionDecrease_Font_Size.setText(QCoreApplication.translate("MainWindow", u"Decrease Font Size", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuAppearance.setTitle(QCoreApplication.translate("MainWindow", u"Appearance", None))
    # retranslateUi

