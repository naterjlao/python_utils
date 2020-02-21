#python3 #TODO need actual shebang!
################################################################################
# File: filterCSV.py
# Author: Nate Lao (lao.nathan@yahoo.com)
# Date: 2-21-2020
# Description:
#	Takes an input csv file and produces a filtered CSV and a remainder CSV 
#   based on keywords specied in filterParams.py.
#	TODO - this is very "hardcoded". In the future, it should be generalized
#          and classes should be taken out to their own file.
#
# Usage:
#     filterCSV.py <CSV_FILE>
################################################################################

import csv
import sys
import re
import filterParams as param

# Utility Functions
def stringListLowercase(strList):
	output = []
	for word in strList:
		output += [word.lower()]
	return output

class DataTable:
	def __init__(self):
		self.headers = []
		self.data = []	
	
	def importFile(self,file):
		list = csv.reader(file)
		isHeaderRow = True
		for row in list:
			if (isHeaderRow):
				self.headers = row
			else:
				self.data += [row] # make sure each row is self-contain in a list
			isHeaderRow = False
	
	# Export to csv
	def exportFile(self,file):
		outFile = csv.writer(file)
		outFile.writerow(self.headers)
		outFile.writerows(self.data)
	
	# Returns the index of the column that matches the <headerName>.
	# Returns -1 if could not be found.
	def getColumnIndex(self,headerName):
		index = 0
		output = -1
		for col in self.headers:
			if (col == headerName):
				output = index
			index += 1
			
		return output
	
	
	# Return the sum amount the data column at <headerName>
	# VERIFIED
	def getColumnSum(self,headerName):
		colIdx = self.getColumnIndex(headerName)
		sum = 0
		for row in self.data:
			sum += float(row[colIdx])
		return sum
	
	# Filter out a keyword from a specified header
	# Returns a tuple of the (filteredTable,remainderTable)
	def filterOut(self,headerName,keywordList):
		filteredTable = DataTable()
		remainderTable = DataTable()
		filteredTable.headers = self.headers
		remainderTable.headers = self.headers
		filteredData = []
		remainderData = []
		keywordList = stringListLowercase(keywordList) # push keywords to lowercase
		colIdx = self.getColumnIndex(headerName)
		
		# Iterate through the input data
		for row in self.data:
			curString = str(row[colIdx]).lower() # pull the target column value, push to lowercase
			containsKeyword = False
			
			# See if the current element contains any of the keywords
			for keyword in keywordList:
				containsKeyword = containsKeyword or (keyword in curString)
			
			# If it does not contain the keyword, push into filtered data
			if (not containsKeyword):
				filteredData += [row]
			# If it does contain the keyword, push to remainder
			else:
				remainderData += [row]		
		
		# Push data to tables
		filteredTable.data = filteredData
		remainderTable.data = remainderData
		
		return (filteredTable,remainderTable)
	
	# Return a format string for headers
	def headersString(self):
		delim = "|"
		numHeaders = len(self.headers)
		output = ""
		i = 0
		while (i < numHeaders):
			output += self.headers[i]
			i += 1
			if (i < numHeaders):
				output += " | "
		return output
		
	def summaryString(self):
		output = ""
		output += "headers:\n%s\n" % self.headersString()
		output += "number of data elements:\n%d\n" % len(self.data)
		return output

# Main runner
if __name__ == "__main__":
	# Open up files
	print("opening %s" % sys.argv[1])
	inputFile = open(sys.argv[1])
	print("opening %s" % param.filteredCSV)
	filteredFile = open(param.filteredCSV, "w+", newline='') # make sure to set newline, it will create extra empty entries
	print("opening %s" % param.remainderCSV)
	remainderFile = open(param.remainderCSV, "w+", newline='')

	# Import data
	print("importing %s" % inputFile)
	dataTable = DataTable()
	dataTable.importFile(inputFile)
	print("INPUT TABLE")
	print(dataTable.summaryString())

	# Perform filtering
	descripHeader = "Transaction Description"
	filteredTable,remainderTable = dataTable.filterOut(descripHeader,param.filterKeywords)
	print("FILTER TABLE")
	print(filteredTable.summaryString())
	print("REMAINDER TABLE")
	print(remainderTable.summaryString())
	
	# Output files
	filteredTable.exportFile(filteredFile)
	remainderTable.exportFile(remainderFile)

	