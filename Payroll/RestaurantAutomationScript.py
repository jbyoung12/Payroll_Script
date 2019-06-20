import csv
import glob
import pandas as pd
import datetime
import imaplib
import email
import os
import shutil

#need python installed
#need to pip install pandas and other stuff above
#need to make Payroll folder with the csv files
#this file should be located in the folder outside of that folder
#to run, on command line, type "python RestaurantAutomationScript.py"

print("Enter your email.")
emailInput = input()
print("Enter your password.")
password = input()
print ("Enter sender's email.")
sender = input()
FROM_EMAIL  = emailInput
FROM_PWD    = password
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993
SENDER = sender

def readmail(sinceDate, endDate):
    shutil.rmtree('CSVs')
    os.makedirs('CSVs')
    # mail reading logic will come here !!
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)

    try:
        mail.login(FROM_EMAIL,FROM_PWD)
    except imaplib.IMAP4.error as e:
        print("Log in failed." + str(e))

    mail.select('inbox')
    if (endDate == ""):
        type, data = mail.search(None, '(FROM "%s")' % (SENDER), '(SINCE "%s")' % (sinceDate))
    else:
        type, data = mail.search(None, '(FROM "%s")' % (SENDER), '(SINCE "%s")' % (sinceDate), '(BEFORE "%s")' % (endDate))
    
    mail_ids = data[0]
    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
    # converts byte literal to string removing b''
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
    # downloading attachments
        for part in email_message.walk():
            # this part comes from the snipped I don't understand yet... 
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            if bool(fileName):
                filePath = os.path.join('./CSVs', fileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()

print("Please enter starting date of emails in format 'day-Month Abbreviated to 3 characters-Year' (e.g. 11-Jun-2019).")
startingDate = input()
print("Please enter end date of emails in same format. Leave blank to read until now.")
endDate = input()
print()
readmail(startingDate, endDate)
path =r'./CSVs'
filenames = glob.glob(path + "/*.csv")
year = datetime.datetime.now().year
filenames.sort()
for filename in filenames:
    if "Retail" in filename:
        restaurantBeginning = filename.find("___")+3
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