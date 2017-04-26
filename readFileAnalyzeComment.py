# Naruth Kongurai
# A tiny script that allows the client to parse in a file and store the
# content in a list that can be used for other purposes.

import csv
import string
from collections import Counter

# Accepts a file in CSV format as a parameter. Returns a dictionary whose keys
# are user IDs and values are a tuple containing the project ID, comment ID,
# and the comment specific to this user
def processData(fileName):
	usersDict = {}
	with open(fileName,"rb") as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			userID = row["user_id"]
			projectID = row["project_id"]
			commentID = row["comment_id"]
			comment = row["comment"]
			tuple = (projectID, commentID, comment)
			
			if userID in usersDict:
				usersDict[userID].append(tuple)
			else:
				usersDict[userID] = [tuple]
				
	return usersDict
	
# Returns a dictionary whose keys are words and values are how many times each
# word occurs.
def countFrequency(usersDict):
	# Retrieves the tuple containing the comment specific to a particular user
	preList = []
	for userID in usersDict.keys():
		for tuple in usersDict[userID]:
			preList.append(tuple[2]) #tuple[2] is the comment!

	# Splits any white spaces from the current list of comments
	spacingSplitList = []
	for sentences in preList:
		spacingSplitList.extend(sentences.split(" "))
		
	# Strips any punctuation from the list of comments
	finalList = []
	for word in spacingSplitList:
		finalList.append(word.strip(string.punctuation))
	
	# Counts frequency of each word occurring and updates frequency dictionary
	wordFrequencyDict = dict(Counter(finalList))
		
	return wordFrequencyDict, finalList
	


fileName = "toyData.csv"

usersDict = processData(fileName)
wordsCountDict, finalList = countFrequency(usersDict)
print wordsCountDict
