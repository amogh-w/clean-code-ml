import numpy as np
import pandas as pd


def add_derived_title(df):
    titles = df['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)

    titles = titles.replace([
        'Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Sir',
        'Jonkheer', 'Dona'
    ], 'Rare')
    titles = titles.replace(['Ms', 'Mlle'], 'Miss')
    titles = titles.replace(['Mme'], 'Mrs')

    df['Totle'] = titles

    return df


def categorize_column(series, num_bins):
    bins = pd.cut(series, num_bins, retbins=True)[1]
    return pd.Series(np.digitize(series, bins, right=True))


def add_is_alone_column(df):
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1

    df['IsAlone'] = 0
    df.loc[df['FamilySize'] == 1, 'IsAlone'] = 1

    df = df.drop(['FamilySize'], axis=1)

    return df


def impute_nans(df, categorical_columns=[], continuous_columns=[]):
    for column in categorical_columns + continuous_columns:
        if column in categorical_columns:
            replacement = df[column].dropna().mode()[0]
        if column in continuous_columns:
            replacement = df[column].dropna().median()
        df[column] = df[column].fillna(replacement)

    return df


def add_categorical_columns(df):
    df = df.copy()

    df['AgeGroup'] = categorize_column(df['Age'], num_bins=5)
    df['FareBand'] = categorize_column(df['Fare'], num_bins=4)
    df['Sex'] = df['Sex'].map({'female': 1, 'male': 0}).astype(int)
    df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2}).astype(int)
    df['Title'] = df['Title'].map({
        "Mr": 1,
        "Miss": 2,
        "Mrs": 3,
        "Master": 4,
        "Rare": 5
    }).fillna(0)

    return df


def train_model(ModelClass, X_train, Y_train, **kwargs):
    model = ModelClass(**kwargs)
    model.fit(X_train, Y_train)

    accuracy_score = round(model.score(X_train, Y_train) * 100, 2)
    print(f'accuracy ({ModelClass.__name__}): {accuracy_score}')

    return model, accuracy_score
