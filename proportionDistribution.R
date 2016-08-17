df<-read.csv("/home/ben/Dropbox/TPM Research Bootcamp/individual-test2-composition.csv", header=FALSE, row.names = 1)
head(df)

highest<-c()
all<-c()

for (i in seq(length(df[,1]))){
  print(i)
  topicNumber<-df[i, c(TRUE,FALSE) ]  # rows)
  topicNumber
  proportion<-df[i, c(FALSE,TRUE) ]  # rows
  speechProp.df<-data.frame(topicNumber = t(topicNumber), proportion=t(proportion))
  highest<-append(highest,(max(proportion)))
  all <- append(all,unlist(proportion))
}

rownames(df)
rownames(speechProp.df)
colnames(speechProp.df)

date<- rownames(df)[1]
date<-strsplit(date, "/")
date[[1]]
date
words <- strsplit(date, "/")[[1]]
words[2]
date<-words[2]
date<-strsplit(date,"\.")[[1]]
date
high.df <- data.frame(topic, mp, year)

hist(highest, breaks = 50)
hist(all, breaks=100)

write.csv(highest,"highest.csv")
write.csv(all,"all.csv")  
#df<-data.frame(topicNumber = t(topicNumber), weightedProportion=t(weightedProportion))
  #rownames(df)<-t(topicNumber)
  #colnames(df)<- c("topicNumber","proportion")
  #df<-df[with(df ,order(-proportion)) ,]
