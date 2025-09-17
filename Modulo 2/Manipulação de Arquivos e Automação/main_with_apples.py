import csv

applesFile = open('apples.csv')
applesReader = csv.reader(applesFile)
applesData = list(applesReader)
applesData

print("\n", applesData[0][0],"-", 
      applesData[0][1],"-",
      applesData[0][2])
print("\n", applesData[1][0], "-",
      applesData[1][1],"-",
      applesData[1][2])
print("\n", applesData[2][0],"-",
      applesData[2][1],"-",
      applesData[2][2])
print("\n", applesData[3][0],"-",
      applesData[3][1],"-",
      applesData[3][2])
print("\n", applesData[4][0],"-",
      applesData[4][1],"-",
      applesData[4][2])
print("\n", applesData[5][0],"-",
      applesData[5][1],"-",
      applesData[5][2])
print("\n", applesData[6][0],"-",
      applesData[6][1],"-",
      applesData[6][2])
print()