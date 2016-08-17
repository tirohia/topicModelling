import os as os
import re
import csv

path="/home/ben/Dropbox/TPM Research Bootcamp/speech-data-2/"
mpList = os.listdir(path)


def group_items(lst):
    res = {}
    reg = re.compile("^(..).*")
    for item in lst:
        match = reg.match(item)
        res.setdefault(match.group(1), []).append(item)
    return len(res.values())


f=open ('countwords.csv', 'wb')
writer = csv.writer(f)


for mp in mpList:
    yearFiles = os.listdir(path+mp)
    for mpFile in yearFiles:
        fileName = path + mp + "/" +  mpFile
        print fileName
        with open(fileName, 'r') as f:
            num_words=0
            for line in f:
                words = line.split()
                num_words += len(words)
        print num_words
        writer.writerow([mp + "/" + mpFile] + [num_words])


