# Import Library
from numpy import sqrt
import pandas as pd
import math

# Defining Class
class dataset:
    def __init__(self):
        # Attributes
        self.name = ""
        self.size = 0
        self.comfort = 0
        self.economical = 0
        self.speed = 0
        self.price = 0
        # Distances
        self.euclid_dist = 0
        self.manhattan_dist = 0
        self.minkowski_dist = 0
        self.supremum_dist = 0
        
# Calculate Euclid Distance
def calculateEuclid(data):
    return (((data.size - 10)**2) + ((data.comfort - 10)**2) + ((data.economical - 10)**2) + ((data.speed - 10)**2) + ((data.price - 0)**2))**(1/2)
    
# Calculate Manhattan Distance
def calculateManhattan(data):
    return abs(data.size - 10) + abs(data.comfort - 10) + abs(data.economical - 10) + abs(data.speed - 10) + abs(data.price - 0)

# Calculate Minkowski Distance
def calculateMinkowski(data):
    return ((abs(data.size - 10)**(3/2)) + (abs(data.comfort - 10)**(3/2)) + (abs(data.economical - 10)**(3/2)) + (abs(data.speed - 10)**(3/2)) + (abs(data.price - 0)**(3/2)))**(2/3)

# Calculate Supremum Distance
def calculateSupremum(data):
    return max(abs(data.size - 10), abs(data.comfort - 10), abs(data.economical - 10), abs(data.speed - 10), abs(data.price - 0))

# Import Data
def imports():
    df = pd.read_csv("mobil.csv")
    return df

# Convert Data
def convert(df):
    arr_ds = []
    for i in range(len(df)):
        temp_ds = dataset()
        temp_ds.name = df.iloc[i][0]
        temp_ds.size = df.iloc[i][1]
        temp_ds.comfort= df.iloc[i][2]
        temp_ds.economical = df.iloc[i][3]
        temp_ds.speed = df.iloc[i][4]
        temp_ds.price = df.iloc[i][5]
        arr_ds.append(temp_ds)
    return arr_ds
    
# Insertion Sort
def insertionSort(arr):
  
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
  
        key = arr[i]
  
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

# Main Program
if __name__ == "__main__": 
    arr_ds = convert(imports())
    
    # Print Each Object
    for obj in arr_ds:
        print("Name : {}, Size : {}, Comfort : {}, Economical : {}, Speed : {}, Price : {}".format(obj.name, obj.size, obj.comfort, obj.economical, obj.speed, obj.price))
    
    # Print Calculation Result of The Object
    print()
    for i in range(len(arr_ds)):
        arr_ds[i].euclid_dist = calculateEuclid(arr_ds[i])
        arr_ds[i].manhattan_dist = calculateManhattan(arr_ds[i])
        arr_ds[i].minkowski_dist = calculateMinkowski(arr_ds[i])
        arr_ds[i].supremum_dist = calculateSupremum(arr_ds[i])
        print("Name : {}, Euclid : {}, Manhattan : {}, Minkowski : {}, Supremum : {}".format(arr_ds[i].name, arr_ds[i].euclid_dist, arr_ds[i].manhattan_dist, arr_ds[i].minkowski_dist, arr_ds[i].supremum_dist))
 
    # Rank The Distance of Each Method
    sorted_euclid = sorted(arr_ds.euclid_dist)
    sorted_manhattan = sorted(arr_ds.manhattan_dist)
    sorted_minkowski = sorted(arr_ds.minkowski_dist)
    sorted_supremum = sorted(arr_ds.supremum_dist)
    

    for obj in sorted_euclid:
        print(obj)



