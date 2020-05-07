#source: https://www.kaggle.com/bhaveshsk/getting-started-with-titanic-dataset/data
#data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

#data visualization
import seaborn as sns
import matplotlib.pyplot as plt

#machine learning packages
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


def prepare_data_and_train_models():

    # In[3]:

    train_df = pd.read_csv("./input/train.csv")
    test_df = pd.read_csv("./input/test.csv")
    df = pd.concat([train_df, test_df])

    df.head()

    # In[4]:

    df = df.drop(['Ticket', 'Cabin'], axis=1)

    # In[5]:

    # [code smell] - Exposed Internals

    df['Title'] = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

    df['Title'] = df['Title'].replace([
        'Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir',
        'Jonkheer', 'Dona'
    ], 'Rare')
    df['Title'] = df['Title'].replace(['Ms', 'Mlle'], 'Miss')
    df['Title'] = df['Title'].replace(['Mme'], 'Mrs')

    # In[6]:

    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

    df['Title'] = df['Title'].map(title_mapping)
    df['Title'] = df['Title'].fillna(0)

    # In[7]:

    # [code smell] Duplicate Responsibility - df.drop() happens at multiple places.
    # it would be better if they were consolidated
    df = df.drop(['Name', 'PassengerId'], axis=1)

    # In[8]:

    # [code smell] Duplicate Responsibility again - encoding of string variables into integers
    # should be consolidated into one place
    df['Sex'] = df['Sex'].map({'female': 1, 'male': 0}).astype(int)

    # In[9]:

    # [code smell] Dead Code - 'AgeBand' column is defined but never used
    df['AgeBand'] = pd.cut(df['Age'], 5)

    # In[10]:

    # [code smell] - magic numbers: 16, 32, 48
    df.loc[df['Age'] <= 16, 'Age'] = 0
    df.loc[(df['Age'] > 16) & (df['Age'] <= 32), 'Age'] = 1
    df.loc[(df['Age'] > 32) & (df['Age'] <= 48), 'Age'] = 2
    df.loc[(df['Age'] > 48) & (df['Age'] <= 64), 'Age'] = 3

    # In[11]:

    df = df.drop(['AgeBand'], axis=1)

    # In[12]:

    # [code smell] Exposed Internals - the next 2 cells could be extracted into a function
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    # In[13]:

    df['IsAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1

    # In[14]:

    df = df.drop(['Parch', 'SibSp', 'FamilySize'], axis=1)

    # In[15]:

    freq_port = df.Embarked.dropna().mode()[0]

    # In[16]:

    df['Embarked'] = df['Embarked'].fillna(freq_port)

    # In[17]:

    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)

    # In[18]:

    # [code smell] Duplicate Responsibility - filling nans with the median value has been done in a cell above
    df['Age'] = df['Age'].fillna(df['Age'].dropna().median())
    df['Fare'] = df['Fare'].fillna(df['Fare'].dropna().median())

    # In[19]:

    # [code smell] Duplication - this looks almost identical to the cells that convert 'Age' from continuous variables to categorical variables
    df['FareBand'] = pd.qcut(df['Fare'], 4)

    # In[20]:

    df.loc[df['Fare'] <= 7.91, 'Fare'] = 0
    df.loc[(df['Fare'] > 7.91) & (df['Fare'] <= 14.454), 'Fare'] = 1
    df.loc[(df['Fare'] > 14.454) & (df['Fare'] <= 31), 'Fare'] = 2
    df.loc[df['Fare'] > 31, 'Fare'] = 3
    df['Fare'] = df['Fare'].astype(int)

    df = df.drop(['FareBand'], axis=1)

    # In[21]:

    train_df = df[-df['Survived'].isna()]
    test_df = df[df['Survived'].isna()]
    test_df = test_df.drop('Survived', axis=1)

    # In[22]:

    X_train = train_df.drop("Survived", axis=1)
    Y_train = train_df["Survived"]
    X_test = test_df.copy()

    # In[23]:

    from src.preprocessing import train_model

    svc, acc_svc = train_model(SVC, X_train, Y_train, gamma='scale')
    knn, acc_knn = train_model(KNeighborsClassifier, X_train, Y_train)
    gaussian, acc_gaussian = train_model(GaussianNB, X_train, Y_train)
    perceptron, acc_perceptron = train_model(Perceptron, X_train, Y_train)
    sgd, acc_sgd = train_model(SGDClassifier, X_train, Y_train)
    decision_tree, acc_decision_tree = train_model(DecisionTreeClassifier,
                                                   X_train, Y_train)
    random_forest, acc_random_forest = train_model(RandomForestClassifier,
                                                   X_train,
                                                   Y_train,
                                                   n_estimators=100)

    return acc_svc, acc_knn, acc_random_forest, acc_gaussian, acc_perceptron, acc_sgd, acc_decision_tree


# In[24]:
#
# models = pd.DataFrame({
# 'Model': [
# 'Support Vector Machines', 'KNN', 'Random Forest', 'Naive Bayes',
# 'Perceptron', 'Stochastic Gradient Decent', 'Decision Tree'
# ],
# 'Score': [
# acc_svc, acc_knn, acc_random_forest, acc_gaussian, acc_perceptron,
# acc_sgd, acc_decision_tree
# ]
# })
# models.sort_values(by='Score', ascending=False)

# In[ ]:
