# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxShowOnlyDifferent = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBoxShowOnlyDifferent.setObjectName("checkBoxShowOnlyDifferent")
        self.horizontalLayout.addWidget(self.checkBoxShowOnlyDifferent)
        self.labelTagFilter = QtWidgets.QLabel(self.centralwidget)
        self.labelTagFilter.setObjectName("labelTagFilter")
        self.horizontalLayout.addWidget(self.labelTagFilter)
        self.lineEditTagFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTagFilter.setObjectName("lineEditTagFilter")
        self.horizontalLayout.addWidget(self.lineEditTagFilter)
        self.labelDescFilter = QtWidgets.QLabel(self.centralwidget)
        self.labelDescFilter.setObjectName("labelDescFilter")
        self.horizontalLayout.addWidget(self.labelDescFilter)
        self.lineEditDescFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditDescFilter.setObjectName("lineEditDescFilter")
        self.horizontalLayout.addWidget(self.lineEditDescFilter)
        self.labelValFilter = QtWidgets.QLabel(self.centralwidget)
        self.labelValFilter.setObjectName("labelValFilter")
        self.horizontalLayout.addWidget(self.labelValFilter)
        self.lineEditValFilter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditValFilter.setObjectName("lineEditValFilter")
        self.horizontalLayout.addWidget(self.lineEditValFilter)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPath = EnhancedQLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPath.sizePolicy().hasHeightForWidth())
        self.labelPath.setSizePolicy(sizePolicy)
        self.labelPath.setMinimumSize(QtCore.QSize(100, 0))
        self.labelPath.setText("")
        self.labelPath.setObjectName("labelPath")
        self.verticalLayout_2.addWidget(self.labelPath)
        self.treeView = DroppableTreeView(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setAcceptDrops(True)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPath_2 = EnhancedQLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPath_2.sizePolicy().hasHeightForWidth())
        self.labelPath_2.setSizePolicy(sizePolicy)
        self.labelPath_2.setMinimumSize(QtCore.QSize(100, 0))
        self.labelPath_2.setText("")
        self.labelPath_2.setObjectName("labelPath_2")
        self.verticalLayout.addWidget(self.labelPath_2)
        self.treeView_2 = DroppableTreeView(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView_2.sizePolicy().hasHeightForWidth())
        self.treeView_2.setSizePolicy(sizePolicy)
        self.treeView_2.setAcceptDrops(True)
        self.treeView_2.setObjectName("treeView_2")
        self.verticalLayout.addWidget(self.treeView_2)
        self.verticalLayout_3.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionDiff = QtWidgets.QAction(MainWindow)
        self.actionDiff.setObjectName("actionDiff")
        self.actionExpand_all = QtWidgets.QAction(MainWindow)
        self.actionExpand_all.setObjectName("actionExpand_all")
        self.actionCollapse_all = QtWidgets.QAction(MainWindow)
        self.actionCollapse_all.setObjectName("actionCollapse_all")
        self.actionText_diff = QtWidgets.QAction(MainWindow)
        self.actionText_diff.setObjectName("actionText_diff")
        self.actionHTML_diff = QtWidgets.QAction(MainWindow)
        self.actionHTML_diff.setObjectName("actionHTML_diff")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAppearance = QtWidgets.QAction(MainWindow)
        self.actionAppearance.setObjectName("actionAppearance")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionDiff)
        self.menuView.addAction(self.actionAppearance)
        self.menuView.addAction(self.actionExpand_all)
        self.menuView.addAction(self.actionCollapse_all)
        self.menuView.addAction(self.actionText_diff)
        self.menuView.addAction(self.actionHTML_diff)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.checkBoxShowOnlyDifferent.setText(_translate("MainWindow", "Only show different"))
        self.labelTagFilter.setText(_translate("MainWindow", "Tag Filter"))
        self.labelDescFilter.setText(_translate("MainWindow", "Description Filter"))
        self.labelValFilter.setText(_translate("MainWindow", "Value filter"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen.setText(_translate("MainWindow", "&Open"))
        self.actionDiff.setText(_translate("MainWindow", "&Diff"))
        self.actionExpand_all.setText(_translate("MainWindow", "&Expand all"))
        self.actionCollapse_all.setText(_translate("MainWindow", "&Collapse all"))
        self.actionText_diff.setText(_translate("MainWindow", "&Text diff"))
        self.actionText_diff.setToolTip(_translate("MainWindow", "Text diff"))
        self.actionHTML_diff.setText(_translate("MainWindow", "&HTML diff"))
        self.actionAbout.setText(_translate("MainWindow", "&About"))
        self.actionAppearance.setText(_translate("MainWindow", "&Appearance"))

from QDICOMDiffer import DroppableTreeView, EnhancedQLabel
