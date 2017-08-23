# compiles information regarding speech length, removes all speeches with less that 100 words. 
# less than was used in the final analysis. 

import os as os
import re
import csv

path="/home/ben/Dropbox/TPM Research Bootcamp/speech-data/"


def group_items(lst):
    res = {}
    reg = re.compile("^(..).*")
    for item in lst:
        match = reg.match(item)
        res.setdefault(match.group(1), []).append(item)
    return len(res.values())


f=open ('speechLengthsGT100.csv', 'wb')
writer = csv.writer(f)

mpList = os.listdir(path)


for mp in mpList:
    print (mp)
    yearFiles = os.listdir(path+mp)

    for mpFile in yearFiles:
        fileName = path  + mp + "/" +  mpFile
        #print mpFile
        num_words=0
        with open(fileName, 'r') as f:
            for line in f:
                words = line.split()
                num_words += len(words)

         
        if(num_words<100):
            os.remove(path + mp + "/" + mpFile)
        #    print (path + mp + "/" + mpFile)
        writer.writerow([ mpFile] + [num_words])


