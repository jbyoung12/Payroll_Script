# Payroll_Script

This script reads CSVs produced for Duke Merchants on Points and adds up the tips for each device/driver.

To Run From Finder:
1. Go into Payroll folder
2. Put payroll CSVs in CSVs folder
2. Double click doPayroll.command
    a. If it says “from unidentified developer”, right click and click open
3. Should open a terminal window (can close that) and a payroll.txt file in TextEdit

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