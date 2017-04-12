# Naruth Kongurai
# Script for reading files and store content + counts words in comments
#

import csv
import string
from collections import Counter

# Write a python program with (at least) two methods: 
# (1) a function that reads files and stores the content in some format
def readStoreFile(fileName):

    #fileName = "/Users/emiliagan/Downloads/toyData.csv"
    commentsList = []
    
    print("\n(1) Importing CSV file: " + fileName)
    print("\n(2) Accessing (reading) the file")

    with open(fileName,"rb") as csvfile:
        commentreader = csv.DictReader(csvfile)
        for row in commentreader:
            commentRow = row["comment"]
            commentsList.append(commentRow) 

    print("\n(3) Storing processed data (comments) as a list")
    print("\n(4) Printing comments in the list:")
    print commentsList

    return commentsList


# (2) a function that then processes the comments and just counts how many times each word occurs. 

def countWordsInComments(commentsList):

    print("(1) Splitting words into its own indices")
    tempCommentsList = []
    for sentences in commentsList:
        tempCommentsList.extend(sentences.split(" "))
    print tempCommentsList
    
    # Removing punctuation
    tempCommentsList2 = []
    for word in tempCommentsList:
        tempCommentsList2.append(word.strip(string.punctuation))
    tempCommentsList = tempCommentsList2

    print("\n(2) Making frequency count for each word")
    occurrencesCounter = Counter(tempCommentsList)
    tempDict = {}
    for word, count in occurrencesCounter.items():
        tempDict[word] = count

    #outputFile.close()
    return tempDict



# commentsList = []

# readStoreFile()

fileName = "/Users/emiliagan/Downloads/toyData.csv"
commentsList = readStoreFile(fileName)

print("\n--------\n")

wordsCountDict = countWordsInComments(commentsList)
print("\n(3) Printing Output:")
print wordsCountDict