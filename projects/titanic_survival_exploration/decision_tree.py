import numpy as np
import pandas as pd

def accuracy_score(truth, pred):
    if len(truth) == len(pred): 
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    else:
        return "Number of predictions does not match number of outcomes!"

def predictions_3(data):
    def fil(passenger):
        if passenger["Sex"] == "female" or passenger["Pclass"] == 1 or (passenger["Age"] < 14 and passenger["SibSp"] < 3):
            return 1
        else:
            return 0
    predictions = data.apply(fil, axis=1)
    return pd.Series(predictions)

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)
predictions = predictions_3(data)
print accuracy_score(outcomes, predictions)

test_file = 'test.csv'
test_set = pd.read_csv(test_file)
predictions = predictions_3(test_set)
predicted_set = test_set.assign(Survived=pd.Series(predictions))
predicted_set = predicted_set[['PassengerId', 'Survived']]
predicted_set.to_csv('results_kaggle.csv', index=False)
print predicted_set.head()
