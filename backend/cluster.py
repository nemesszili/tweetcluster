from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

from matplotlib import pyplot as plt

from PyQt5 import QtCore
class Clusterizer():
    def __init__(self):
        super(self.__class__, self).__init__()
        self.km = None
        self.tf_idf_matrix = None
        self.stemmer = None
        self.vectorizer = None
    def stemmer(self, text):
        self.stemmer = PorterStemmer()
        tokens = word_tokenize(text)
        tokens = [w.lower() for w in tokens if w.isalnum()]
        stems = []
        for item in tokens:
            stems.append(self.stemmer.stem(item))
        return stems

    def tf_idf(self, tweets):
        self.vectorizer = TfidfVectorizer(tokenizer=self.stemmer, stop_words='english')
        self.tf_idf_matrix = self.vectorizer.fit_transform(tweets)

    def k_means(self, number_of_clusters):
        self.km = KMeans(n_clusters=number_of_clusters, init='k-means++', max_iter=100, n_init=1, verbose=False)
        self.km.fit(self.tf_idf_matrix)

    def plot_k_means(self, pl):
        model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
        svd = model.fit_transform(self.tf_idf_matrix)
        pl.scatter(svd[:, 0], svd[:, 1], c=self.km.labels_)

    def plot_complete(self, pl):
        model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
        svd = model.fit_transform(self.tf_idf_matrix)
        Z = linkage(svd, 'complete')
        dendrogram(Z,  leaf_font_size=8, truncate_mode='lastp', p=100, orientation='top', no_labels=True, ax=pl)
        pl.plot()

    def plot_single(self, pl):
        model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
        svd = model.fit_transform(self.tf_idf_matrix)
        Z = linkage(svd, 'single')
        dendrogram(Z,  leaf_font_size=8, truncate_mode='lastp', p=30, orientation='top', ax=pl)
        pl.plot()

    def getKMLabels(self, number_of_clusters):
        labels = ""
        order_centroids = self.km.cluster_centers_.argsort()[:, ::-1]
        terms = self.vectorizer.get_feature_names()
        for i in range(number_of_clusters):
            for ind in order_centroids[i, :10]:
                labels = labels + str(terms[ind])
                labels = labels + "\n"
        return labels

# nem biztos hogy itt kell, --> main 
# def getTweets():
#     for j in range(len(tweets['data'])):
#         if km.labels_[j] == i:
#             print('{}: '.format(count), end='')
#             print(tweets['data'][j])
#     print('\n')



# import numbers

# print("Top terms per cluster:")

# avgs = [0] * N_clusters
# counts = [0] * N_clusters

# terms = vectorizer.get_feature_names()

# # Calculate average tf-idf values for each cluster
# for i in range(N_clusters):
#     for j in range(len(tweets)):
#         if Z.labels_[j] == i:
#             if isinstance(avgs[i], numbers.Number):
#                 avgs[i] = X[j].toarray()
#             else:
#                 avgs[i] += X[j].toarray()
#             counts[i] += 1
            
# for i in range(len(avgs)):
#     avgs[i] = avgs[i] / counts[i]
    
# avgs = np.asarray(avgs).argsort()[:, 0, ::-1]

# for i in range(N_clusters):
#     print("Cluster %d:" % i)
#     for j in avgs[i, :10]:
#         print(' %s' % terms[j])
#     count = 0
#     for j in range(len(tweets)):
#         if Z.labels_[j] == i:
#             count += 1
#             print('{}: '.format(count))
#             print(tweets[j])
#             print("\n")
