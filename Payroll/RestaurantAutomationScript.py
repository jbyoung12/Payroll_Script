import csv
import glob
import pandas as pd
import datetime


#need python installed
#need to pip install pandas and other stuff above
#need to make Payroll folder with the csv files
#this file should be located in the folder outside of that folder
#to run, on command line, type "python RestaurantAutomationScript.py"

path =r'./CSVs'
filenames = glob.glob(path + "/*.csv")
year = datetime.datetime.now().year

for filename in filenames:
    if "Retail" in filename:
        restaurantBeginning = filename.find("___")+3;
        restaurantEnd = filename.find("___", restaurantBeginning+1)
        restaurant = filename[restaurantBeginning:restaurantEnd]
        restaurant = restaurant.replace("_", " ")
        print(restaurant)
        location = filename.find(str(year))
        today = filename[location:location+10]
        # print (restaurant)
        print (today)
        df = pd.read_csv(filename)
        totalTips = {}
        totalRevenue = 0
        for index, row in df.iterrows():
            if not isinstance(row['POS Name'], float):
                if restaurant in row['POS Name']:
                        if "Tips" in row['Tender Name']:
                            posname = row['POS Name'].split(' ') #Sushi Love 4, 4 would be posname[2]
                            if posname[2] in totalTips:
                                totalTips[posname[2]] += int(round(float(row['Retail Tran Tender Amount'].strip('$'))*100))
                            else:
                                totalTips[posname[2]] = int(round(float(row['Retail Tran Tender Amount'].strip('$'))*100))

        for key, value in totalTips.items():
            print("driver {0} tips: {1}".format(key, '${:,.2f}'.format(value/100.0)))
        print()