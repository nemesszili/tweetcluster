import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets

from frontend import main_window_design
from backend.tweet import getTweets, MAX_QUERY
from backend.cluster import tf_idf, k_means, plot_k_means, plot_single, plot_complete

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MainWindow(QtWidgets.QMainWindow, main_window_design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.tweets = None
        self.thread = None
        self.progressLabel.setText("Standby")
        self._connectsignals()

        #Canvas for plotting
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.groupBox_4)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.groupBox_4.setLayout(layout)
        self.pl = self.figure.add_subplot(111)

    def _connectsignals(self):
        self.tweetButton.clicked.connect(self._tweetButton)
        self.clusterButton.clicked.connect(self._clusterButton)
        self.clusterCombo.currentIndexChanged.connect(self._clusterChanged)

    def _tweetButton(self):
        if self.thread is None:
            if self.queryEdit.text():
                self.progressLabel.setText("Fetching tweets...")
                self.thread = TweetThread(self.queryEdit.text(), self.nrTweet.value())
                self.thread.finished.connect(self._tweetOver)
                self.thread.start()
            else:
                self.progressLabel.setText("Please provide a query!")

    def _tweetOver(self):
        self.progressLabel.setText("Done fetching tweets!")
        self.thread = None

    def _clusterButton(self):
        if self.thread is None:
            self.progressLabel.setText("Clustering...")
            self.thread = ClusterThread(self.algCombo.currentText(), 2, self.pl)
            self.thread.finished.connect(self._clusterOver)
            self.thread.start()

    def _clusterOver(self):
        self.canvas.draw()
        self.progressLabel.setText("Done clustering!")
        self.thread = None

    def _clusterChanged(self):
        print ("changed")


class TweetThread(QtCore.QThread):
    def __init__(self, query, nrTweet):
        super(self.__class__, self).__init__()
        self.query = query
        self.nrTweet = nrTweet

    def run(self):
        self.query = self.query.split(',')[:MAX_QUERY]
        self.tweets = []
        for q in self.query:
            self.tweets += getTweets(q, self.nrTweet)
        with open('tweet.json', 'w') as f:
            json.dump(self.tweets, f)

class ClusterThread(QtCore.QThread):
    def __init__(self, alg_combo_value, cluster_size, pl):
        super(self.__class__, self).__init__()
        self.alg_combo_value = alg_combo_value
        self.cluster_size = cluster_size
        self.pl = pl

    def run(self):
        datastore = None
        with open('tweet.json', 'r') as f:
            datastore = json.load(f)
        tf_idf_matrix = tf_idf(datastore)        
        self.pl.clear()
        if self.alg_combo_value == "KMeans":
            km = k_means(tf_idf_matrix, self.cluster_size)
            plot_k_means(tf_idf_matrix, km, self.pl)
        if self.alg_combo_value == "Single linkage":
            plot_single(tf_idf_matrix, self.pl)
        if self.alg_combo_value == "Complete linkage":
            plot_complete(tf_idf_matrix, self.pl)
         
            

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()    

if __name__ == '__main__':
    main()