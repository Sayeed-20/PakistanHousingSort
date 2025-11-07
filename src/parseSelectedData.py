import pandas as pd
from dataset import Dataset

df = pd.read_csv("pakistanHousingData_cleaned.csv")
df["bedrooms"] = df["bedrooms"].astype(str)
df["baths"] = df["baths"].astype(str)

def parseSelectedData(df, cityDict, propDict, bedDict, bathDict):

    for key in cityDict:
        if cityDict[key] == False:
            df = df[df["city"] != key]

    for key in propDict:
        if propDict[key] == False:
            df = df[df["property_type"] != key]

    for key in bedDict:
        if bedDict[key] == False:
            df = df[df["bedrooms"] != key]

    for key in bathDict:
        if bathDict[key] == False:
            df = df[df["baths"] != key]

    df = df.reset_index(drop=True)

    return Dataset(df)


def getSelectedData(df, cityDict, propDict, bedDict, bathDict):

    for key in cityDict:
        if cityDict[key] == False:
            df = df[df["city"] != key]

    for key in propDict:
        if propDict[key] == False:
            df = df[df["property_type"] != key]

    for key in bedDict:
        if bedDict[key] == False:
            df = df[df["bedrooms"] != key]

    for key in bathDict:
        if bathDict[key] == False:
            df = df[df["baths"] != key]

    df = df.reset_index(drop=True)

    return df

# Testing:

# selectedData = parseSelectedData(df, cities, propertyTypes, bedrooms, bathrooms)
# for house in selectedData.data:
#     print(house);