import pubmed_parser as pub
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


experiment_datetime_version = "2020-05-02-joem_v1"

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
data["coord_x"] =  dimensions[:,0]
data["coord_y"] =  dimensions[:,1]

# Saving scatterplot to image:
plt.figure(figsize=(20,10))
plt.ylim(-40,40)
groups = data.groupby("cluster")
for name, group in groups:
    plt.plot(group["coord_x"], group["coord_y"], marker="o", linestyle="", label=name)
plt.title("All JOEM Articles, displayed by cluster")
plt.legend()
plt.savefig(experiment_datetime_version + ".png")
plt.show()

# saving to a csv file
data.to_csv(experiment_datetime_version + ".csv", index=None)
