import pubmed_parser as pub
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE


# loading data from xml
data = pub.get_dataframe().dropna()

# Extracting bag of word features
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(data.abstract)

# clusterizing features
kmeans = KMeans(n_clusters=20, random_state=0).fit(X)

data["cluster"] = kmeans.labels_

# Adding tsne vector coordinates
dimensions = TSNE(n_components=2).fit_transform(features.toarray())

