# Project Signups Tool for MESA

## Background and Problem
MESA stands for Mathematics, Engineering, Science, and Achievement. I'm the President of MESA at our school and every year, we have the problem of sorting huge spreadsheets of which competitions every person wants to enter.

We either manually sift through the data or spend lots of time creating spreadsheet rules and scripts to sort our data.

## Solution
This simple Python script filters through our spreadsheet (signups.xlsx (read more below)) and outputs the project name alongside who wants to sign up for it!

## Spreadsheet (signups.xlsx)
This mock spreadsheet contains 6 columns (Name, Machine, Glider, Tank, Bridge, Arm). Here's a brief description of each one:
* Name: Letters and letters + numbers used as "names"
* Machine, Glider, Tank, Bridge, Arm: Shorthand names of our competitions

Note: Binary scheme for project signups (0 = would NOT like to sign up, 1 = WANTS to sign up). This random binary matrix was generated using GNU Octave.

## Set Up
This program has a simple setup. Simply make sure you run
`pip3 install xlrd` for Excel spreadsheet support and
`pip3 install pandas` for Pandas support!
