import pandas

titanic = pandas.read_csv("train.csv")

# print(titanic.head(5))
# print(titanic.describe())

# fill missing ages with median age
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())

# change male sex to 0, female sex to 1
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1
#print(titanic["Sex"].unique())

# fill missing port with S, then convert to numerical factors
titanic["Embarked"] = titanic["Embarked"].fillna("S")
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2
print(titanic["Embarked"].unique())

