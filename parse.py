import csv

file = "./SWAG Sales - Pre-Event Fundraisers.csv"

friends = "Friends of GeoWoodstock"
bdb = "Black Diamond Backers"

friendsList = []
bdbList = []

with open(file, 'r') as file:
  csvreader = csv.reader(file)
  next(csvreader)

  for row in csvreader:
    sponsorType = row[11]
    cacherName = row[13].strip()

    if sponsorType == friends:
      friendsList.append(cacherName)
    elif sponsorType == bdb:
      bdbList.append(cacherName)

print("")
print(friends)
print(friendsList)

print("")
print(bdb)
print(bdbList)