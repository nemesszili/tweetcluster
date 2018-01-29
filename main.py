import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal

from frontend import main_window_design
from backend.tweet import getTweets, MAX_QUERY
from backend.cluster import Clusterizer

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
                self.thread.emitter.connect(self._print_labels)
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
            number_of_clusters = self.nrClusters.value()
            cluster_type = self.algCombo.currentText()
            self.thread = ClusterThread(cluster_type, number_of_clusters, self.pl, self.labelsView)
            self.thread.labelEmitter.connect(self._get_labels)
            self.clusterCombo.clear()
            for i in range(1, number_of_clusters+1):
                self.clusterCombo.addItem(str(i))
            # self.labelsView.setText(self.thread.getKMLabels())
            self.thread.finished.connect(self._clusterOver)
            self.thread.start()

    def _clusterOver(self):
        self.canvas.draw()
        self.progressLabel.setText("Done clustering!")
        self.thread = None

    def _clusterChanged(self):
        try:
            index = int(self.clusterCombo.currentText())-1
            self.labelsView.setText(self.labels[index])
            self.tweetView.setText(self.clusteredTweets[index])
        except Exception as ex:
            print("Combobox value inited, not real error")

    def _get_labels(self, labels, clusteredTweets):
        self.labels = labels
        self.clusteredTweets = clusteredTweets
        self.labelsView.setText(labels[0])
        self.tweetView.setText(clusteredTweets[0])
        # self.clusterCombo


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

class ClusterThread(QtCore.QThread, QObject):

    labelEmitter = pyqtSignal(object, object)

    def __init__(self, alg_combo_value, number_of_clusters, pl, lab_view):
        super(self.__class__, self).__init__()
        self.alg_combo_value = alg_combo_value
        self.number_of_clusters = number_of_clusters
        self.pl = pl
        self.cluster_class = Clusterizer()
        self.lab_view = lab_view

    def run(self):
        tweets = None
        with open('tweet.json', 'r') as f:
            tweets = json.load(f)
        self.cluster_class.tf_idf(tweets)
        self.pl.clear()
        labels = None
        clusteredTweets = None
        if self.alg_combo_value == "KMeans":
            self.cluster_class.k_means(self.number_of_clusters)
            labels, clusteredTweets = self.cluster_class.getKMLabels(self.number_of_clusters)
            self.cluster_class.plot_k_means(self.pl)
        elif self.alg_combo_value == "Ward linkage":
            self.cluster_class.calculateWardLabels(self.number_of_clusters)
            self.cluster_class.plot_ward(self.number_of_clusters, self.pl)
            labels, clusteredTweets = self.cluster_class.getWard_CompleteLabels(self.number_of_clusters)
        elif self.alg_combo_value == "Complete linkage":
            self.cluster_class.calculateCompleteLabels(self.number_of_clusters)
            self.cluster_class.plot_complete(self.number_of_clusters, self.pl)
            labels, clusteredTweets = self.cluster_class.getWard_CompleteLabels(self.number_of_clusters)
        self.labelEmitter.emit(labels, clusteredTweets)

def main():
    app = QtWidgets.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()    

if __name__ == '__main__':
    main()