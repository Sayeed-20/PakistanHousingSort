from house import House
import pandas as pd
import mergesort

class Dataset:

    def __init__(self, df, sortOrder = "unsorted"):
        self.data = []
        for i in range(len(df)):
            id = df.iloc[i]["property_id"]
            price = df.iloc[i]["price"]
            city = df.iloc[i]["city"]
            propType = df.iloc[i]["property_type"]
            long = df.iloc[i]["longitude"]
            lat = df.iloc[i]["latitude"]
            bedrooms = df.iloc[i]["bedrooms"]
            baths = df.iloc[i]["baths"]

            newHouse = House(id, price, city, propType, long, lat, bedrooms, baths)
            self.data.append(newHouse)

    def changeSortStatus(self, sortOrder):
        self.sortOrder = sortOrder
        # During initialization: will change sortOrder accordingly
        #e.g. initialize ascending quicksort will: quicksort(arr ...) and dataset.changeSortStatus(ascending)

    def flipSortStatus(self):
        if self.sortOrder == "ascending":
            self.sortOrder = "descending"
        elif self.sortOrder == "descending":
            self.sortOrder = "ascending"