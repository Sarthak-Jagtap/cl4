# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Display dataset
print("Dataset:\n")
print(df.head())

# Features for clustering
X = df

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)

# Train model
kmeans.fit(X)

# Predict cluster labels
clusters = kmeans.predict(X)

# Add cluster column to DataFrame
df['Cluster'] = clusters

# Display clustered dataset
print("\nDataset with Cluster Labels:\n")
print(df.head())

# Display cluster centers
print("\nCluster Centers:\n")
print(kmeans.cluster_centers_)

# ---------------- CLUSTERING METRICS ----------------

# Inertia
print("\nInertia:")
print(kmeans.inertia_)

# Silhouette Score
sil_score = silhouette_score(X, clusters)

print("\nSilhouette Score:")
print(sil_score)

# ---------------- CLUSTER VISUALIZATION ----------------

plt.figure(figsize=(8,6))

# Plot clustered data points
scatter = plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    c=df['Cluster']
)

# Plot centroids
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=200,
    marker='X',
    label='Centroids'
)

# Labels
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")

# Title
plt.title("K-Means Clustering on Iris Dataset")

# Legend
plt.legend()

# Show plot
plt.show()