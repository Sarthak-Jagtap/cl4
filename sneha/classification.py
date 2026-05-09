# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target column
df['target'] = iris.target

# Display first 5 rows
print("Dataset:\n")
print(df.head())

# Features and target
X = df.drop('target', axis=1)
y = df['target']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Create SVM classifier
model = SVC(kernel='linear')

# Train model
model.fit(X_train, y_train)

# Predict output
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

# Display outputs
print("\nPredicted Values:")
print(y_pred)

print("\nActual Values:")
print(y_test.values)

print("\nAccuracy:")
print(accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ---------------- VISUALIZATION ----------------

# Scatter plot using first two features
plt.figure(figsize=(8,6))

scatter = plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    c=df['target']
)

# Labels
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.title("Iris Flower Classification")

# Legend
plt.legend(
    handles=scatter.legend_elements()[0],
    labels=list(iris.target_names)
)

plt.show()

