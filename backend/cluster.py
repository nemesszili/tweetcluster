from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans, AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

import numbers
import np

class Clusterizer():
	def __init__(self):
		self.km = None
		self.tf_idf_matrix = None
		self.stemmer = None
		self.vectorizer = None
		self.tweets = None

	def stemmer(self, text):
		self.stemmer = PorterStemmer()
		tokens = word_tokenize(text)
		tokens = [w.lower() for w in tokens if w.isalnum()]
		stems = []
		for item in tokens:
			stems.append(self.stemmer.stem(item))
		return stems

	def tf_idf(self, tweets):
		self.tweets = tweets
		self.vectorizer = TfidfVectorizer(tokenizer=self.stemmer, stop_words='english')
		self.tf_idf_matrix = self.vectorizer.fit_transform(tweets)

	def k_means(self, number_of_clusters):
		self.km = KMeans(n_clusters=number_of_clusters, init='k-means++', max_iter=100, n_init=1, verbose=False)
		self.km.fit(self.tf_idf_matrix)

	def plot_k_means(self, pl):
		model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
		svd = model.fit_transform(self.tf_idf_matrix)
		pl.scatter(svd[:, 0], svd[:, 1], c=self.km.labels_)

	def plot_complete(self, number_of_clusters, pl):
		model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
		svd = model.fit_transform(self.tf_idf_matrix)
		Z = linkage(svd, 'complete')
		dendrogram(Z,  leaf_font_size=8, truncate_mode='lastp', p=100, orientation='top', no_labels=True, ax=pl)
		pl.plot()

	def plot_ward(self, number_of_clusters, pl):
		model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
		svd = model.fit_transform(self.tf_idf_matrix)
		Z = linkage(svd, 'ward')
		dendrogram(Z,  leaf_font_size=8, truncate_mode='lastp', p=100, orientation='top', no_labels=True, ax=pl)
		pl.plot()

	def calculateWardLabels(self, number_of_clusters):
		Z = AgglomerativeClustering(n_clusters=number_of_clusters, linkage="ward")
		Z.fit_predict(self.tf_idf_matrix.toarray())
		self.Z = Z

	def calculateCompleteLabels(self, number_of_clusters):
		Z = AgglomerativeClustering(n_clusters=number_of_clusters, linkage="complete")
		Z.fit_predict(self.tf_idf_matrix.toarray())
		self.Z = Z

	def getWard_CompleteLabels(self, number_of_clusters):
		avgs = [0] * number_of_clusters
		counts = [0] * number_of_clusters

		terms = self.vectorizer.get_feature_names()

		# Calculate average tf-idf values for each cluster
		for i in range(number_of_clusters):
			for j in range(len(self.tweets)):
				if self.Z.labels_[j] == i:
					if isinstance(avgs[i], numbers.Number):
						avgs[i] = self.tf_idf_matrix[j].toarray()
					else:
						avgs[i] += self.tf_idf_matrix[j].toarray()
					counts[i] += 1
					
		for i in range(len(avgs)):
			avgs[i] = avgs[i] / counts[i]
			
		avgs = np.asarray(avgs).argsort()[:, 0, ::-1]

		labels = []
		clusteredTweets = []
		for i in range(number_of_clusters):
			labels.append("")
			clusteredTweets.append("")
			for j in avgs[i, :10]:
				labels[i] += terms[j] + "\n"
			count = 0
			for j in range(len(self.tweets)):
				if self.Z.labels_[j] == i:
					count += 1
					clusteredTweets[i] += "{}: {}\n".format(count, repr(self.tweets[j]))
		return labels, clusteredTweets


	def getKMLabels(self, number_of_clusters):
		labels = []
		clusteredTweets = []
		order_centroids = self.km.cluster_centers_.argsort()[:, ::-1]
		terms = self.vectorizer.get_feature_names()

		for i in range(number_of_clusters):
			labels.append("")
			for ind in order_centroids[i, :10]:
				labels[i] = labels[i] + str(terms[ind])
				labels[i] = labels[i] + "\n"
			
			count = 0
			clusteredTweets.append("")
			for j in range(len(self.tweets)):
				if self.km.labels_[j] == i:
					count += 1
					oneTweet = '{}: {}\n'.format(count, repr(self.tweets[j]))
					clusteredTweets[i] += oneTweet
		return labels, clusteredTweets
