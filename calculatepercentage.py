# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load the data from URL
url = "http://bit.ly/w-data"
data = pd.read_csv(url)

# plot the data to visualize the relationship
data.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Scored')
plt.show()

# divide the data into attributes (inputs) and labels (outputs)
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# train the linear regression model on the training data
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predict the percentage for the test data
y_pred = regressor.predict(X_test)

# compare the actual and predicted values
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)

# predict the percentage for a custom input value
hours = 9.25
custom_pred = regressor.predict([[hours]])
print("Number of hours studied = {}".format(hours))
print("Predicted percentage = {}".format(custom_pred[0]))
