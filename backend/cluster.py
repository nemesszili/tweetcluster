from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage

def stemmer(text):
    stemmer = PorterStemmer()
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens if w.isalnum()]
    stems = []
    for item in tokens:
        stems.append(stemmer.stem(item))
    return stems

def tf_idf(tweets):
    vectorizer = TfidfVectorizer(tokenizer=stemmer, stop_words='english')
    tf_idf_matrix = vectorizer.fit_transform(tweets)
    return tf_idf_matrix

def k_means(tf_idf_matrix ,cluster_size):
    km = KMeans(n_clusters=cluster_size, init='k-means++', max_iter=100, n_init=1, verbose=False)
    km.fit(tf_idf_matrix)
    return km

def plot_k_means(tf_idf_matrix, km, pl):
    model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
    svd = model.fit_transform(tf_idf_matrix)
    pl.scatter(svd[:, 0], svd[:, 1], c=km.labels_)

def plot_complete(tf_idf_matrix, pl):
    model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
    svd = model.fit_transform(tf_idf_matrix)
    Z = linkage(svd, 'complete')
    dendrogram(Z,  leaf_font_size=8, truncate_mode='lastp', p=100, orientation='top', no_labels=True)
    print ("here")

    # pl.plot()

def plot_single(tf_idf_matrix, pl):
    model = TruncatedSVD(n_components=2, algorithm='randomized', n_iter=100, tol=0.0)
    svd = model.fit_transform(tf_idf_matrix)
    Z = linkage(svd, 'single')
    dendrogram(Z,  leaf_font_size=8, truncate_mode='lastp', p=30, orientation='top')
    # pl.plot()