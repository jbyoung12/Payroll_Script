# Payroll_Script

This script reads CSVs produced for Duke Merchants on Points and adds up the tips for each device/driver.

The user enters his gmail, password, the sender it wants attachments from, and the starting and ending date, and it downloads the attachments between 2 dates and does the payroll.

To Run From Finder:
1. Go to Tech Stuff
2. Download Payroll.zip
3. Open it/Unzip it
4. Double click doPayroll.command
	a. If it says “from unidentified developer”, right click and click open
5. Should open a terminal window prompting you. Enter email, password, and sender.
	a. Enter the date you want to start checking emails. This is not the CSV date but the date the email was sent to us. The format must look like 1-Jun-2019 (3 letter abbreviation for the month, Jun can be lowercase, need 4 digit year).
	b. Enter the date you want to stop checking emails in the same format as above. Can leave blank and just click enter to check until now. 
6. payroll.txt file should open in TextEdit with the payroll done.


To Wrap Into Executable:
1. Download PyInstaller (can run pip install pyinstaller)
2. Run pyinstaller RestaurantAutomationScript.py
3. Copy RestaurantAutomationScript directory inside of dist directory into Payroll directory

To Run From Command Line:
1. run cd Payroll
2. Put payroll CSVs in CSVs folder
2. run ./doPayroll.command
3. Should open payroll.txt file in TextEdit

To Run Using Python:
1. cd Payroll
2. Download Python3 (if you don't already have it)
3. Install following packages by running pip install <package name> 
    a. pandas
    b. glob
    c. csv
    d. datetime
4. Put payroll CSVs in CSVs folder
5. Run Python RestaurantAutomationScript.py
6. Should print out to console the CSVs