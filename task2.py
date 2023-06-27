import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = {
    'Id': [1, 2, 3, 4, 5],
    'SepalLengthCm': [5.1, 4.9, 4.7, 4.6, 5.0],
    'SepalWidthCm': [3.5, 3.0, 3.2, 3.1, 3.6],
    'PetalLengthCm': [1.4, 1.4, 1.3, 1.5, 1.4],
    'PetalWidthCm': [0.2, 0.2, 0.2, 0.2, 0.2],
    'Species': ['Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa', 'Iris-setosa']
}
df = pd.DataFrame(data)

# Assign features and target variable
X = df.drop(['Id', 'Species'], axis=1)  # Features
y = df['Species']  # Target variable

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the decision tree classifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Predict the class labels for the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
