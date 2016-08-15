import os as os
import re
import csv


## reads a directory containing a directory for each mp, 
## each of which contains a file with all speeches from each year
## groups on the 1st 2 digits of the file names (parliament), counts
## and outputs mp name and number of parliaments that mp was a member of
## to a csv file  
path="/home/ben/Dropbox/TPM Research Bootcamp/speech-data-2/"
mpList = os.listdir(path)


def group_items(lst):
    res = {}
    reg = re.compile("^(..).*")
    for item in lst:
        match = reg.match(item)
        res.setdefault(match.group(1), []).append(item)
    return len(res.values())

f=open ('countTerms.csv', 'wb')
writer = csv.writer(f)

for mp in mpList:
    yearFiles = os.listdir(path+mp)
    writer.writerow([mp] + [group_items(yearFiles)])


