import pandas as pd
import tkinter as tk
from parseSelectedData import parseSelectedData
from dictionaries import selectedCities, selectedBathrooms, selectedBedrooms, selectedPropTypes

# Read dataset
df = pd.read_csv("pakistanHousingData_cleaned.csv") # Not needed here, should be in main
df["bedrooms"] = df["bedrooms"].astype(str)
df["baths"] = df["baths"].astype(str)


# ----- Front End -----


# Initialize Window
window = tk.Tk()
window.title("Pakistani Property Sorter")
window.geometry("800x400")



# City selection
cityLabel = tk.Label(window, text="Cities")
cityLabel.place(x=550, y=30)

cityBox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=4)
for key in selectedCities:
    cityBox.insert(tk.END, key)

def toggleCityDropdown():
    if cityBox.winfo_viewable():
        cityBox.place_forget()
    else:
        cityBox.place(x=550, y=80)
        cityBox.lift()

def updateSelectedCities(event):
    selected = [cityBox.get(i) for i in cityBox.curselection()]
    for key in selectedCities:
        if key in selected:
            selectedCities[key] = True
        else:
            selectedCities[key] = False
        print("key: ", key, "val: ", selectedCities[key])

cityBox.bind("<<ListboxSelect>>", updateSelectedCities)
cityDropdown = tk.Button(window, text="Select Cities:", command=toggleCityDropdown)
cityDropdown.place(x=550, y=50)



# Property Type selection
propTypeLabel = tk.Label(window, text="Property Types")
propTypeLabel.place(x=550, y=110)

propTypeBox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=4)
for key in selectedPropTypes:
    propTypeBox.insert(tk.END, key)

def togglePropTypeDropdown():
    if propTypeBox.winfo_viewable():
        propTypeBox.place_forget()
    else:
        propTypeBox.place(x=550, y=160)
        propTypeBox.lift()

def updateSelectedPropTypes(event):
    selected = [propTypeBox.get(i) for i in propTypeBox.curselection()]
    for key in selectedPropTypes:
        if key in selected:
            selectedPropTypes[key] = True
        else:
            selectedPropTypes[key] = False
        print("key: ", key, "val: ", selectedPropTypes[key])

propTypeBox.bind("<<ListboxSelect>>", updateSelectedPropTypes)
propTypeDropdown = tk.Button(window, text="Select Property Types:", command=togglePropTypeDropdown)
propTypeDropdown.place(x=550, y=130)



# Bedrooms selection
bedroomsLabel = tk.Label(window, text="Bedrooms")
bedroomsLabel.place(x=550, y=190)

bedroomsBox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=4)
for key in selectedBedrooms:
    if key == "68":
        continue
    bedroomsBox.insert(tk.END, key)

def toggleBedroomsDropdown():
    if bedroomsBox.winfo_viewable():
        bedroomsBox.place_forget()
    else:
        bedroomsBox.place(x=550, y=240)
        bedroomsBox.lift()

def updateSelectedBedrooms(event):
    selected = [bedroomsBox.get(i) for i in bedroomsBox.curselection()]
    for key in selectedBedrooms:
        if key in selected:
            selectedBedrooms[key] = True
        else:
            selectedBedrooms[key] = False
        print("Bedroom: ", key, "Selected: ", selectedBedrooms[key])

bedroomsBox.bind("<<ListboxSelect>>", updateSelectedBedrooms)
bedroomsDropdown = tk.Button(window, text="Select Bedrooms:", command=toggleBedroomsDropdown)
bedroomsDropdown.place(x=550, y=210)


# Bathrooms selection
bathroomsLabel = tk.Label(window, text="Bathrooms")
bathroomsLabel.place(x=550, y=270)

bathroomsBox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=4)
for key in selectedBathrooms:
    if key == "403":
        continue
    bathroomsBox.insert(tk.END, key)

def toggleBathroomsDropdown():
    if bathroomsBox.winfo_viewable():
        bathroomsBox.place_forget()
    else:
        bathroomsBox.place(x=550, y=320)
        bathroomsBox.lift()

def updateSelectedBathrooms(event):
    selected = [bathroomsBox.get(i) for i in bathroomsBox.curselection()]
    for key in selectedBathrooms:
        if key in selected:
            selectedBathrooms[key] = True
        else:
            selectedBathrooms[key] = False
        print("Bathroom: ", key, "Selected: ", selectedBathrooms[key])

bathroomsBox.bind("<<ListboxSelect>>", updateSelectedBathrooms)
bathroomsDropdown = tk.Button(window, text="Select Bathrooms:", command=toggleBathroomsDropdown)
bathroomsDropdown.place(x=550, y=290)



# Initialize data
def initializeWithMerge():
    print("happening")
    selectedData = parseSelectedData(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms)
    #call merge on selectedData
    for i in selectedData.data:
        print(i)

def initializeWithQuick():
    selectedData = parseSelectedData(df, selectedCities, selectedPropTypes, selectedBedrooms, selectedBathrooms)
    #call merge on selectedData
    for i in selectedData.data:
        print("seen", i)

mergeInitButton = tk.Button(window, text="Initialize with Merge Sort", command=initializeWithMerge)
mergeInitButton.place(anchor = "w", x = 500, y = 250)

quickInitButton = tk.Button(window, text="Initialize with Quick Sort", command=initializeWithQuick)
quickInitButton.place(anchor = "w", x = 500, y = 350)


window.mainloop()