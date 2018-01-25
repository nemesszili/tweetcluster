import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from frontend import main_window_design

class MainWindow(QtWidgets.QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self._connectsignals()

    def _connectsignals(self):
        self.tweetButton.clicked.connect(self._tweetButton)
        self.clusterButton.clicked.connect(self._clusterButton)
        self.clusterCombo.currentIndexChanged.connect(self._clusterChanged)

    def _tweetButton(self):
        print "tweet"

    def _clusterButton(self):
        print "cluster"

    def _clusterChanged(self):
        print "changed"
    

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()    

if __name__ == '__main__':
    main()