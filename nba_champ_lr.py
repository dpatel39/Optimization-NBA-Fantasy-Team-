
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pandas as pd

team_features = pd.read_csv('team_features.csv')
x = team_features.drop(['team', 'year'], axis = 1)
y = team_features.champion

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)
predictions = logisticRegr.predict(x_test)
score = logisticRegr.score(x_test, y_test)
print(score)

cm = metrics.confusion_matrix(y_test, predictions)
print(cm)

print(logisticRegr.coef_)

