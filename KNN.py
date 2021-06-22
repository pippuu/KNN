# Import Library
from numpy import sqrt
import pandas as pd
import xlsxwriter

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
        # Score for Voting
        self.score = 0

# Import Data
def imports(target):
    df = pd.read_csv(target)
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

# Preprocess
def normalize(arr):
    # Finding Min-Max each Attribute
    min = [10, 10, 10, 10, 999999]
    max = [0, 0, 0, 0, 0]
    for i in range(len(arr)):
        if arr[i].size < min[0]:
            min[0] = arr[i].size
        if arr[i].comfort < min[1]:
            min[1] = arr[i].comfort
        if arr[i].economical < min[2]:
            min[2] = arr[i].economical
        if arr[i].speed < min[3]:
            min[3] = arr[i].speed
        if arr[i].price < min[4]:
            min[4] = arr[i].price
        if arr[i].size > max[0]:
            max[0] = arr[i].size
        if arr[i].comfort > max[1]:
            max[1] = arr[i].comfort
        if arr[i].economical > max[2]:
            max[2] = arr[i].economical
        if arr[i].speed > max[3]:
            max[3] = arr[i].speed
        if arr[i].price > max[4]:
            max[4] = arr[i].price

    # Normalize
    for i in range(len(arr)):
        arr[i].size = (arr[i].size-min[0])*(10/(max[0]-min[0]))
        arr[i].comfort = (arr[i].comfort-min[1])*(10/(max[1]-min[1]))
        arr[i].economical = (arr[i].economical-min[2])*(10/(max[2]-min[2]))
        arr[i].speed = (arr[i].speed-min[3])*(10/(max[3]-min[3]))
        arr[i].price = (arr[i].price-min[4])*(10/(max[4]-min[4]))
    return arr
    
# Calculate Euclid Distance
def calculateEuclid(data, userPref):
    return (((data.size - userPref.size)**2) + ((data.comfort - userPref.comfort)**2) + ((data.economical - userPref.economical)**2) + ((data.speed - userPref.speed)**2) + ((data.price - userPref.price)**2))**(1/2)
    
# Calculate Manhattan Distance
def calculateManhattan(data, userPref):
    return abs(data.size - userPref.size) + abs(data.comfort - userPref.comfort) + abs(data.economical - userPref.economical) + abs(data.speed - userPref.speed) + abs(data.price - userPref.price)

# Calculate Minkowski Distance
def calculateMinkowski(data, userPref):
    return ((abs(data.size - userPref.size)**(3/2)) + (abs(data.comfort - userPref.comfort)**(3/2)) + (abs(data.economical - userPref.economical)**(3/2)) + (abs(data.speed - userPref.speed)**(3/2)) + (abs(data.price - userPref.price)**(3/2)))**(2/3)

# Calculate Supremum Distance
def calculateSupremum(data, userPref):
    return max(abs(data.size - userPref.size), abs(data.comfort - userPref.comfort), abs(data.economical - userPref.economical), abs(data.speed - userPref.speed), abs(data.price - userPref.price))

# Insertion Sort
def insertionSort(arr_ds):
    a, b, c, d = arr_ds.copy(), arr_ds.copy(), arr_ds.copy(), arr_ds.copy()
    # Euclid
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >=0 and key.euclid_dist < a[j].euclid_dist :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = key
    # Manhattan
    for i in range(1, len(b)):
        key = b[i]
        j = i-1
        while j >=0 and key.manhattan_dist < b[j].manhattan_dist :
                b[j+1] = b[j]
                j -= 1
        b[j+1] = key
    # Minkowski
    for i in range(1, len(c)):
        key = c[i]
        j = i-1
        while j >=0 and key.minkowski_dist < c[j].minkowski_dist :
                c[j+1] = c[j]
                j -= 1
        c[j+1] = key
    # Supremum
    for i in range(1, len(d)):
        key = d[i]
        j = i-1
        while j >=0 and key.supremum_dist < d[j].supremum_dist :
                d[j+1] = d[j]
                j -= 1
        d[j+1] = key
    return a, b, c, d

# Export Data
def exports(arr, target):
    workbook = xlsxwriter.Workbook(target)
    worksheet = workbook.add_worksheet()

    row = 0
    col = 0

    for i in range(3):
        worksheet.write(row, col, arr[i].name)
        row += 1

    workbook.close()

# Main Program
if __name__ == "__main__":

    # Import Training Data
    print("Importing mobil.xls...")
    arr_ds = convert(imports("mobil.csv"))

    # Import Test Data
    print("Importing test.xls...")
    user_df = imports("test.csv")
    userPref = dataset()
    userPref.size = user_df.iloc[0][1]
    userPref.comfort = user_df.iloc[0][2]
    userPref.economical = user_df.iloc[0][3]
    userPref.speed = user_df.iloc[0][4]
    userPref.price = user_df.iloc[0][5]
    arr_ds.append(userPref)
    print()

    # Preprocessing Data
    print("Preprocessing data...")
    arr_ds = normalize(arr_ds)
    userPref = arr_ds[17]
    arr_ds.pop(17)
    print("Preprocessing complete.")
    print()
    
    # Print Each Object
    print("Normalized data:")
    for obj in arr_ds:
        print("Name : {}, Size : {}, Comfort : {}, Economical : {}, Speed : {}, Price : {}".format(obj.name, obj.size, obj.comfort, obj.economical, obj.speed, obj.price))
    print()

    # Calculate and Print Distances per Method
    print("Calculating distances...")
    print("Calculation result:")
    for i in range(len(arr_ds)):
        arr_ds[i].euclid_dist = calculateEuclid(arr_ds[i], userPref)
        arr_ds[i].manhattan_dist = calculateManhattan(arr_ds[i], userPref)
        arr_ds[i].minkowski_dist = calculateMinkowski(arr_ds[i], userPref)
        arr_ds[i].supremum_dist = calculateSupremum(arr_ds[i], userPref)
        print("Name : {}, Euclid : {}, Manhattan : {}, Minkowski : {}, Supremum : {}".format(arr_ds[i].name, arr_ds[i].euclid_dist, arr_ds[i].manhattan_dist, arr_ds[i].minkowski_dist, arr_ds[i].supremum_dist))
    print()

    # Sort per Method
    print("Sorting each method...")
    sorted_euclid, sorted_manhattan, sorted_minkowski, sorted_supremum = insertionSort(arr_ds)
    print()
    print("Highest three in euclid method:")
    for i in range(3):
        print("Name : {}, Euclid : {}".format(sorted_euclid[i].name, sorted_euclid[i].euclid_dist))
    print()
    print("Highest three in manhattan method:")
    for i in range(3):
        print("Name : {}, Manhattan : {}".format(sorted_manhattan[i].name, sorted_manhattan[i].manhattan_dist))
    print()
    print("Highest three in minkowski method:")
    for i in range(3):
        print("Name : {}, Minkowski : {}".format(sorted_minkowski[i].name, sorted_minkowski[i].minkowski_dist))
    print()
    print("Highest three in supremum method:")
    for i in range(3):
        print("Name : {}, Supremum : {}".format(sorted_supremum[i].name, sorted_supremum[i].supremum_dist))
    
    # Export Data
    print()
    print("Exporting data...")
    exports(sorted_euclid, "rekomendasi_euclidean.xls")
    exports(sorted_manhattan, "rekomendasi_manhattan.xls")
    exports(sorted_minkowski, "rekomendasi_minkowski.xls")
    exports(sorted_supremum, "rekomendasi_supremum.xls")
    print()
    print("Exporting done.")