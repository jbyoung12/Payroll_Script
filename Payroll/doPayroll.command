#!/bin/bash
cd "`dirname "$0"`"
rm payroll.txt
touch payroll.txt
./RestaurantAutomationScript/RestaurantAutomationScript | tee payroll.txt
open -a TextEdit payroll.txt
