# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaintWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PaintWindow(object):
    def setupUi(self, PaintWindow):
        PaintWindow.setObjectName("PaintWindow")
        PaintWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(PaintWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox_BrushSize = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_BrushSize.setGeometry(QtCore.QRect(660, 50, 125, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_BrushSize.setFont(font)
        self.comboBox_BrushSize.setObjectName("comboBox_BrushSize")
        self.comboBox_BrushSize.addItem("")
        self.comboBox_BrushSize.addItem("")
        self.comboBox_BrushSize.addItem("")
        self.comboBox_BrushSize.addItem("")
        self.comboBox_BrushSize.addItem("")
        self.comboBox_BrushSize.addItem("")
        self.comboBox_BrushColor = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_BrushColor.setGeometry(QtCore.QRect(660, 120, 125, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_BrushColor.setFont(font)
        self.comboBox_BrushColor.setObjectName("comboBox_BrushColor")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.comboBox_BrushColor.addItem("")
        self.label_BrushSize = QtWidgets.QLabel(self.centralwidget)
        self.label_BrushSize.setGeometry(QtCore.QRect(660, 20, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_BrushSize.setFont(font)
        self.label_BrushSize.setObjectName("label_BrushSize")
        self.label_BrushColor = QtWidgets.QLabel(self.centralwidget)
        self.label_BrushColor.setGeometry(QtCore.QRect(660, 90, 125, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_BrushColor.setFont(font)
        self.label_BrushColor.setObjectName("label_BrushColor")
        self.label_Instruments = QtWidgets.QLabel(self.centralwidget)
        self.label_Instruments.setGeometry(QtCore.QRect(660, 160, 125, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Instruments.setFont(font)
        self.label_Instruments.setObjectName("label_Instruments")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(660, 200, 131, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.BrushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BrushButton.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/paint-brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BrushButton.setIcon(icon)
        self.BrushButton.setObjectName("BrushButton")
        self.verticalLayout.addWidget(self.BrushButton)
        self.PenButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.PenButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/pencil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PenButton.setIcon(icon1)
        self.PenButton.setObjectName("PenButton")
        self.verticalLayout.addWidget(self.PenButton)
        self.EraserButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.EraserButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EraserButton.setIcon(icon2)
        self.EraserButton.setObjectName("EraserButton")
        self.verticalLayout.addWidget(self.EraserButton)
        self.DropperButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DropperButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/pipette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DropperButton.setIcon(icon3)
        self.DropperButton.setObjectName("DropperButton")
        self.verticalLayout.addWidget(self.DropperButton)
        self.LineButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LineButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LineButton.setIcon(icon4)
        self.LineButton.setObjectName("LineButton")
        self.verticalLayout.addWidget(self.LineButton)
        self.RectangleButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RectangleButton.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/rectangle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RectangleButton.setIcon(icon5)
        self.RectangleButton.setObjectName("RectangleButton")
        self.verticalLayout.addWidget(self.RectangleButton)
        self.CircleButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.CircleButton.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CircleButton.setIcon(icon6)
        self.CircleButton.setObjectName("CircleButton")
        self.verticalLayout.addWidget(self.CircleButton)
        self.ClearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ClearButton.setFont(font)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/clear-mop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ClearButton.setIcon(icon7)
        self.ClearButton.setObjectName("ClearButton")
        self.verticalLayout.addWidget(self.ClearButton)
        self.label_CurentColor = QtWidgets.QLabel(self.centralwidget)
        self.label_CurentColor.setGeometry(QtCore.QRect(660, 510, 131, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_CurentColor.setFont(font)
        self.label_CurentColor.setText("")
        self.label_CurentColor.setObjectName("label_CurentColor")
        PaintWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PaintWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menuSave.setFont(font)
        self.menuSave.setObjectName("menuSave")
        PaintWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PaintWindow)
        self.statusbar.setObjectName("statusbar")
        PaintWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(PaintWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveImageAs = QtWidgets.QAction(PaintWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionSaveImageAs.setFont(font)
        self.actionSaveImageAs.setObjectName("actionSaveImageAs")
        self.actionOpen = QtWidgets.QAction(PaintWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_to_my_files = QtWidgets.QAction(PaintWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionSave_to_my_files.setFont(font)
        self.actionSave_to_my_files.setObjectName("actionSave_to_my_files")
        self.actionOpen_from_my_files = QtWidgets.QAction(PaintWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionOpen_from_my_files.setFont(font)
        self.actionOpen_from_my_files.setObjectName("actionOpen_from_my_files")
        self.actionExit = QtWidgets.QAction(PaintWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.menuSave.addAction(self.actionOpen)
        self.menuSave.addAction(self.actionSaveImageAs)
        self.menuSave.addAction(self.actionSave_to_my_files)
        self.menuSave.addAction(self.actionOpen_from_my_files)
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(PaintWindow)
        QtCore.QMetaObject.connectSlotsByName(PaintWindow)

    def retranslateUi(self, PaintWindow):
        _translate = QtCore.QCoreApplication.translate
        PaintWindow.setWindowTitle(_translate("PaintWindow", "MainWindow"))
        self.comboBox_BrushSize.setItemText(0, _translate("PaintWindow", "2px"))
        self.comboBox_BrushSize.setItemText(1, _translate("PaintWindow", "4px"))
        self.comboBox_BrushSize.setItemText(2, _translate("PaintWindow", "8px"))
        self.comboBox_BrushSize.setItemText(3, _translate("PaintWindow", "12px"))
        self.comboBox_BrushSize.setItemText(4, _translate("PaintWindow", "16px"))
        self.comboBox_BrushSize.setItemText(5, _translate("PaintWindow", "32px"))
        self.comboBox_BrushColor.setItemText(0, _translate("PaintWindow", "White"))
        self.comboBox_BrushColor.setItemText(1, _translate("PaintWindow", "Black"))
        self.comboBox_BrushColor.setItemText(2, _translate("PaintWindow", "Dark Gray"))
        self.comboBox_BrushColor.setItemText(3, _translate("PaintWindow", "Gray"))
        self.comboBox_BrushColor.setItemText(4, _translate("PaintWindow", "Light Gray"))
        self.comboBox_BrushColor.setItemText(5, _translate("PaintWindow", "Red"))
        self.comboBox_BrushColor.setItemText(6, _translate("PaintWindow", "Green"))
        self.comboBox_BrushColor.setItemText(7, _translate("PaintWindow", "Blue"))
        self.comboBox_BrushColor.setItemText(8, _translate("PaintWindow", "Cyan"))
        self.comboBox_BrushColor.setItemText(9, _translate("PaintWindow", "Magenta"))
        self.comboBox_BrushColor.setItemText(10, _translate("PaintWindow", "Yellow"))
        self.comboBox_BrushColor.setItemText(11, _translate("PaintWindow", "Dark Red"))
        self.comboBox_BrushColor.setItemText(12, _translate("PaintWindow", "Dark Green"))
        self.comboBox_BrushColor.setItemText(13, _translate("PaintWindow", "Dark Blue"))
        self.comboBox_BrushColor.setItemText(14, _translate("PaintWindow", "Dark Cyan"))
        self.comboBox_BrushColor.setItemText(15, _translate("PaintWindow", "Dark Magenta"))
        self.comboBox_BrushColor.setItemText(16, _translate("PaintWindow", "Dark Yellow"))
        self.label_BrushSize.setText(_translate("PaintWindow", "Brush Size"))
        self.label_BrushColor.setText(_translate("PaintWindow", "Brush Color"))
        self.label_Instruments.setText(_translate("PaintWindow", "Instruments"))
        self.BrushButton.setText(_translate("PaintWindow", "Brush"))
        self.PenButton.setText(_translate("PaintWindow", "Pencil"))
        self.EraserButton.setText(_translate("PaintWindow", "Eraser"))
        self.DropperButton.setText(_translate("PaintWindow", "Dropper"))
        self.LineButton.setText(_translate("PaintWindow", "Line"))
        self.RectangleButton.setText(_translate("PaintWindow", "Rectangle"))
        self.CircleButton.setText(_translate("PaintWindow", "Circle"))
        self.ClearButton.setText(_translate("PaintWindow", "Clear Canvas"))
        self.menuSave.setTitle(_translate("PaintWindow", "File"))
        self.actionSave.setText(_translate("PaintWindow", "Save"))
        self.actionSaveImageAs.setText(_translate("PaintWindow", "Save As..."))
        self.actionOpen.setText(_translate("PaintWindow", "Open"))
        self.actionSave_to_my_files.setText(_translate("PaintWindow", "Save to your Folder"))
        self.actionOpen_from_my_files.setText(_translate("PaintWindow", "Open from your files"))
        self.actionExit.setText(_translate("PaintWindow", "Exit App"))
import resources_rc
