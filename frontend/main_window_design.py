# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 594)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 330, 261, 181))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.tweetButton = QtWidgets.QPushButton(self.groupBox)
        self.tweetButton.setGeometry(QtCore.QRect(80, 110, 81, 31))
        self.tweetButton.setObjectName("tweetButton")
        self.queryEdit = QtWidgets.QLineEdit(self.groupBox)
        self.queryEdit.setGeometry(QtCore.QRect(90, 30, 151, 20))
        self.queryEdit.setObjectName("queryEdit")
        self.nrTweet = QtWidgets.QSpinBox(self.groupBox)
        self.nrTweet.setGeometry(QtCore.QRect(90, 70, 61, 22))
        self.nrTweet.setMinimum(1)
        self.nrTweet.setMaximum(5000)
        self.nrTweet.setObjectName("nrTweet")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(300, 330, 231, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.algCombo = QtWidgets.QComboBox(self.groupBox_2)
        self.algCombo.setGeometry(QtCore.QRect(90, 30, 111, 22))
        self.algCombo.setObjectName("algCombo")
        self.algCombo.addItem("")
        self.algCombo.addItem("")
        self.algCombo.addItem("")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 61, 21))
        self.label_3.setObjectName("label_3")
        self.clusterButton = QtWidgets.QPushButton(self.groupBox_2)
        self.clusterButton.setGeometry(QtCore.QRect(60, 110, 81, 31))
        self.clusterButton.setObjectName("clusterButton")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(540, 10, 571, 541))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tweetView = QtWidgets.QListWidget(self.groupBox_3)
        self.tweetView.setGeometry(QtCore.QRect(10, 20, 551, 291))
        self.tweetView.setObjectName("tweetView")
        self.labelsView = QtWidgets.QListView(self.groupBox_3)
        self.labelsView.setGeometry(QtCore.QRect(10, 340, 131, 191))
        self.labelsView.setObjectName("labelsView")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 320, 51, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(160, 320, 51, 21))
        self.label_5.setObjectName("label_5")
        self.infoView = QtWidgets.QListView(self.groupBox_3)
        self.infoView.setGeometry(QtCore.QRect(160, 340, 271, 191))
        self.infoView.setObjectName("infoView")
        self.clusterCombo = QtWidgets.QComboBox(self.groupBox_3)
        self.clusterCombo.setGeometry(QtCore.QRect(450, 400, 91, 31))
        self.clusterCombo.setObjectName("clusterCombo")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(450, 360, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 10, 521, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 501, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 530, 61, 16))
        self.label_7.setObjectName("label_7")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(70, 530, 141, 16))
        self.progressLabel.setText("")
        self.progressLabel.setObjectName("progressLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TweetCluster"))
        self.groupBox.setTitle(_translate("MainWindow", "Tweets"))
        self.label.setText(_translate("MainWindow", "Query:"))
        self.label_2.setText(_translate("MainWindow", "Nr. of tweets:"))
        self.tweetButton.setText(_translate("MainWindow", "Get tweets"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Clustering"))
        self.algCombo.setItemText(0, _translate("MainWindow", "KMeans"))
        self.algCombo.setItemText(1, _translate("MainWindow", "Single linkage"))
        self.algCombo.setItemText(2, _translate("MainWindow", "Complete linkage"))
        self.label_3.setText(_translate("MainWindow", "Algorithm:"))
        self.clusterButton.setText(_translate("MainWindow", "Clusterize"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Results"))
        self.label_4.setText(_translate("MainWindow", "Labels"))
        self.label_5.setText(_translate("MainWindow", "Info"))
        self.label_6.setText(_translate("MainWindow", "Select cluster:"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Visual"))
        self.label_7.setText(_translate("MainWindow", "Progress:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

